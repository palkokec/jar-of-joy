/**
 * Jar of Joy - Core Application Logic
 * Handles localStorage operations and data management
 */

const JarOfJoy = (function() {
    'use strict';

    const STORAGE_KEY = 'jarOfJoy_sparks';
    const SETTINGS_KEY = 'jarOfJoy_settings';

    // Initialize
    function init() {
        // Check if localStorage is available
        if (!isLocalStorageAvailable()) {
            console.error('localStorage is not available');
            alert('Your browser does not support localStorage. Data will not be saved.');
            return false;
        }
        return true;
    }

    // Check localStorage availability
    function isLocalStorageAvailable() {
        try {
            const test = '__localStorage_test__';
            localStorage.setItem(test, test);
            localStorage.removeItem(test);
            return true;
        } catch(e) {
            return false;
        }
    }

    // Get all sparks
    function getSparks() {
        try {
            const data = localStorage.getItem(STORAGE_KEY);
            return data ? JSON.parse(data) : [];
        } catch(e) {
            console.error('Error reading sparks:', e);
            return [];
        }
    }

    // Save sparks
    function saveSparks(sparks) {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(sparks));
            return true;
        } catch(e) {
            console.error('Error saving sparks:', e);
            alert('Failed to save data. Your storage might be full.');
            return false;
        }
    }

    // Add a new spark
    function addSpark(spark) {
        const sparks = getSparks();
        sparks.push(spark);
        return saveSparks(sparks);
    }

    // Delete a spark by ID
    function deleteSpark(sparkId) {
        const sparks = getSparks();
        const filtered = sparks.filter(spark => spark.id !== sparkId);
        return saveSparks(filtered);
    }

    // Get spark by ID
    function getSparkById(sparkId) {
        const sparks = getSparks();
        return sparks.find(spark => spark.id === sparkId);
    }

    // Calculate streak (consecutive days with sparks)
    function calculateStreak() {
        const sparks = getSparks();
        if (sparks.length === 0) return 0;

        // Sort sparks by date (newest first)
        const sortedSparks = sparks.sort((a, b) => 
            new Date(b.timestamp) - new Date(a.timestamp)
        );

        let streak = 0;
        let currentDate = new Date();
        currentDate.setHours(0, 0, 0, 0);

        // Check if there's a spark today or yesterday
        const lastSparkDate = new Date(sortedSparks[0].timestamp);
        lastSparkDate.setHours(0, 0, 0, 0);
        
        const daysDiff = Math.floor((currentDate - lastSparkDate) / (1000 * 60 * 60 * 24));
        
        if (daysDiff > 1) {
            return 0; // Streak broken
        }

        // Count consecutive days
        let checkDate = new Date(lastSparkDate);
        
        for (let i = 0; i < sortedSparks.length; i++) {
            const sparkDate = new Date(sortedSparks[i].timestamp);
            sparkDate.setHours(0, 0, 0, 0);
            
            if (sparkDate.getTime() === checkDate.getTime()) {
                streak++;
                checkDate.setDate(checkDate.getDate() - 1);
            } else if (sparkDate < checkDate) {
                break;
            }
        }

        return streak;
    }

    // Export data as JSON
    function exportData() {
        const sparks = getSparks();
        const settings = getSettings();
        
        const exportData = {
            version: '1.0',
            exportDate: new Date().toISOString(),
            sparks: sparks,
            settings: settings
        };

        const dataStr = JSON.stringify(exportData, null, 2);
        const dataBlob = new Blob([dataStr], { type: 'application/json' });
        
        const url = URL.createObjectURL(dataBlob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `jar-of-joy-backup-${new Date().toISOString().split('T')[0]}.json`;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    }

    // Import data from JSON
    function importData(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            
            reader.onload = function(e) {
                try {
                    const data = JSON.parse(e.target.result);
                    
                    if (!data.sparks || !Array.isArray(data.sparks)) {
                        reject(new Error('Invalid backup file format'));
                        return;
                    }

                    // Merge with existing data or replace
                    const shouldMerge = confirm('Do you want to merge with existing data? Click Cancel to replace all data.');
                    
                    if (shouldMerge) {
                        const existingSparks = getSparks();
                        const mergedSparks = [...existingSparks, ...data.sparks];
                        saveSparks(mergedSparks);
                    } else {
                        saveSparks(data.sparks);
                    }

                    if (data.settings) {
                        saveSettings(data.settings);
                    }

                    resolve(data.sparks.length);
                } catch(error) {
                    reject(error);
                }
            };

            reader.onerror = function() {
                reject(new Error('Failed to read file'));
            };

            reader.readAsText(file);
        });
    }

    // Clear all data
    function clearAllData() {
        if (confirm('Are you sure you want to delete all your sparks? This cannot be undone!')) {
            localStorage.removeItem(STORAGE_KEY);
            localStorage.removeItem(SETTINGS_KEY);
            return true;
        }
        return false;
    }

    // Settings management
    function getSettings() {
        try {
            const data = localStorage.getItem(SETTINGS_KEY);
            return data ? JSON.parse(data) : {
                language: 'en',
                theme: 'auto'
            };
        } catch(e) {
            return { language: 'en', theme: 'auto' };
        }
    }

    function saveSettings(settings) {
        try {
            localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings));
            return true;
        } catch(e) {
            console.error('Error saving settings:', e);
            return false;
        }
    }

    // Get storage usage info
    function getStorageInfo() {
        const sparks = getSparks();
        const sparksSize = new Blob([JSON.stringify(sparks)]).size;
        const totalSize = sparksSize;
        
        return {
            sparkCount: sparks.length,
            storageUsed: (totalSize / 1024).toFixed(2) + ' KB',
            storageUsedBytes: totalSize
        };
    }

    // Public API
    return {
        init,
        getSparks,
        addSpark,
        deleteSpark,
        getSparkById,
        calculateStreak,
        exportData,
        importData,
        clearAllData,
        getSettings,
        saveSettings,
        getStorageInfo
    };
})();

// Initialize on load
document.addEventListener('DOMContentLoaded', function() {
    JarOfJoy.init();
});

// Backup reminder (show every 30 days)
function checkBackupReminder() {
    const REMINDER_KEY = 'jarOfJoy_lastBackupReminder';
    const lastReminder = localStorage.getItem(REMINDER_KEY);
    const now = Date.now();
    const thirtyDays = 30 * 24 * 60 * 60 * 1000;

    if (!lastReminder || (now - parseInt(lastReminder)) > thirtyDays) {
        const sparks = JarOfJoy.getSparks();
        if (sparks.length > 10) {
            setTimeout(() => {
                if (confirm('💾 Backup Reminder: You have ' + sparks.length + ' sparks saved. Would you like to create a backup now?')) {
                    JarOfJoy.exportData();
                }
                localStorage.setItem(REMINDER_KEY, now.toString());
            }, 2000);
        }
    }
}

// Check backup reminder on dashboard
if (window.location.pathname.endsWith('index.html') || window.location.pathname.endsWith('/')) {
    checkBackupReminder();
}

// Made with Bob
