"""
Configuration file for Jar of Joy multilingual support
"""

LANGUAGES = {
    'en': {
        'name': 'English',
        'code': 'en',
        'dir': 'ltr',
        'translations': {
            # Meta
            'site_title': 'Jar of Joy',
            'site_description': 'Capture and revisit your moments of gratitude, joy, and inspiration throughout the year.',
            'site_keywords': 'gratitude journal, joy jar, thankfulness, memories, inspiration, quotes, mindfulness',
            
            # Navigation
            'nav_home': 'Home',
            'nav_reveal': 'Reveal',
            'nav_collection': 'Collection',
            'nav_add': 'Add',
            
            # Dashboard
            'dashboard_title': 'Dashboard',
            'today_reflection': "Today's Reflection",
            'sparks_collected': 'Sparks Collected',
            'jar_status': 'Your Jar is {percent}% Full',
            'jar_description': "You've been capturing moments of gratitude consistently. Each spark represents a memory that made your heart smile.",
            'add_spark_button': 'Add a Spark of Joy',
            'recent_sparks': 'Recent Sparks',
            'view_collection': 'View Collection',
            'streak_label': 'Streak',
            'streak_days': '{days} Days',
            'joy_level_label': 'Joy Level',
            'joy_level_value': 'Radiant',
            
            # Add Spark
            'add_spark_title': 'Add a Spark of Joy',
            'add_spark_subtitle': 'Capture this moment of gratitude',
            'spark_type_label': 'Type',
            'spark_type_memory': 'Memory',
            'spark_type_quote': 'Quote',
            'spark_type_gratitude': 'Gratitude',
            'spark_type_achievement': 'Achievement',
            'spark_content_label': 'Your Spark',
            'spark_content_placeholder': 'What made you smile today?',
            'spark_tags_label': 'Tags (optional)',
            'spark_tags_placeholder': 'nature, friends, peace...',
            'spark_image_label': 'Add Image (optional)',
            'save_spark': 'Save Spark',
            'cancel': 'Cancel',
            
            # Reveal
            'reveal_title': 'Moment of Reflection',
            'reveal_subtitle': 'Rediscover a spark from your collection',
            'reveal_button': 'Reveal Another',
            'no_sparks': 'Your jar is empty. Start adding sparks of joy!',
            'reveal_date': 'Captured on',
            
            # Collection
            'collection_title': 'Your Collection',
            'collection_subtitle': 'All your sparks of joy',
            'filter_all': 'All',
            'filter_memory': 'Memories',
            'filter_quote': 'Quotes',
            'filter_gratitude': 'Gratitude',
            'filter_achievement': 'Achievements',
            'search_placeholder': 'Search your sparks...',
            'sort_newest': 'Newest First',
            'sort_oldest': 'Oldest First',
            'sort_random': 'Random',
            'empty_collection': 'No sparks found',
            
            # Settings
            'settings_title': 'Settings',
            'language_label': 'Language',
            'theme_label': 'Theme',
            'theme_light': 'Light',
            'theme_dark': 'Dark',
            'theme_auto': 'Auto',
            'backup_title': 'Backup & Restore',
            'backup_description': 'Your data is stored locally in your browser. Export it to keep a backup.',
            'export_data': 'Export Data',
            'import_data': 'Import Data',
            'clear_data': 'Clear All Data',
            'clear_confirm': 'Are you sure? This cannot be undone.',
            
            # Footer
            'footer_text': 'Made with ❤️ for spreading joy',
            'backup_instructions': 'Backup Instructions',
            'backup_info_title': 'How to Backup Your Data',
            'backup_info_text': 'Your sparks are stored locally in your browser. To backup your data, open your browser\'s Developer Tools (F12), go to Application/Storage tab, find Local Storage, and copy the "jar-of-joy-sparks" data. Save it to a text file for safekeeping.',
        }
    },
    'sk': {
        'name': 'Slovenčina',
        'code': 'sk',
        'dir': 'ltr',
        'translations': {
            # Meta
            'site_title': 'Pohár Radosti',
            'site_description': 'Zachytávajte a znovu objavujte svoje momenty vďačnosti, radosti a inšpirácie počas celého roka.',
            'site_keywords': 'denník vďačnosti, pohár radosti, vďačnosť, spomienky, inšpirácia, citáty, všímavosť',
            
            # Navigation
            'nav_home': 'Domov',
            'nav_reveal': 'Odhaliť',
            'nav_collection': 'Zbierka',
            'nav_add': 'Pridať',
            
            # Dashboard
            'dashboard_title': 'Prehľad',
            'today_reflection': 'Dnešná úvaha',
            'sparks_collected': 'Zozbieraných spomienok',
            'jar_status': 'Váš pohár je {percent}% plný',
            'jar_description': 'Konzistentne zachytávate momenty vďačnosti. Každá spomienka predstavuje moment, ktorý vám rozžiaril srdce.',
            'add_spark_button': 'Pridať spomienku radosti',
            'recent_sparks': 'Nedávne spomienky',
            'view_collection': 'Zobraziť zbierku',
            'streak_label': 'Séria',
            'streak_days': '{days} dní',
            'joy_level_label': 'Úroveň radosti',
            'joy_level_value': 'Žiarivá',
            
            # Add Spark
            'add_spark_title': 'Pridať spomienku radosti',
            'add_spark_subtitle': 'Zachyťte tento moment vďačnosti',
            'spark_type_label': 'Typ',
            'spark_type_memory': 'Spomienka',
            'spark_type_quote': 'Citát',
            'spark_type_gratitude': 'Vďačnosť',
            'spark_type_achievement': 'Úspech',
            'spark_content_label': 'Vaša spomienka',
            'spark_content_placeholder': 'Čo vás dnes rozosmialo?',
            'spark_tags_label': 'Štítky (voliteľné)',
            'spark_tags_placeholder': 'príroda, priatelia, pokoj...',
            'spark_image_label': 'Pridať obrázok (voliteľné)',
            'save_spark': 'Uložiť spomienku',
            'cancel': 'Zrušiť',
            
            # Reveal
            'reveal_title': 'Moment zamyslenia',
            'reveal_subtitle': 'Znovu objavte spomienku zo svojej zbierky',
            'reveal_button': 'Odhaliť ďalšiu',
            'no_sparks': 'Váš pohár je prázdny. Začnite pridávať spomienky radosti!',
            'reveal_date': 'Zachytené',
            
            # Collection
            'collection_title': 'Vaša zbierka',
            'collection_subtitle': 'Všetky vaše spomienky radosti',
            'filter_all': 'Všetko',
            'filter_memory': 'Spomienky',
            'filter_quote': 'Citáty',
            'filter_gratitude': 'Vďačnosť',
            'filter_achievement': 'Úspechy',
            'search_placeholder': 'Hľadať vo vašich iskrách...',
            'sort_newest': 'Najnovšie',
            'sort_oldest': 'Najstaršie',
            'sort_random': 'Náhodne',
            'empty_collection': 'Nenašli sa žiadne spomienky',
            
            # Settings
            'settings_title': 'Nastavenia',
            'language_label': 'Jazyk',
            'theme_label': 'Téma',
            'theme_light': 'Svetlá',
            'theme_dark': 'Tmavá',
            'theme_auto': 'Automatická',
            'backup_title': 'Zálohovanie a obnovenie',
            'backup_description': 'Vaše údaje sú uložené lokálne vo vašom prehliadači. Exportujte ich pre zálohu.',
            'export_data': 'Exportovať údaje',
            'import_data': 'Importovať údaje',
            'clear_data': 'Vymazať všetky údaje',
            'clear_confirm': 'Ste si istí? Toto sa nedá vrátiť späť.',
            
            # Footer
            'footer_text': 'Vytvorené s ❤️ pre šírenie radosti',
            'backup_instructions': 'Pokyny na zálohovanie',
            'backup_info_title': 'Ako zálohovať vaše údaje',
            'backup_info_text': 'Vaše spomienky sú uložené lokálne vo vašom prehliadači. Pre zálohovanie údajov otvorte Vývojárske nástroje prehliadača (F12), prejdite na záložku Application/Storage, nájdite Local Storage a skopírujte údaje "jar-of-joy-sparks". Uložte ich do textového súboru pre bezpečné uchovanie.',
        }
    }
}

DEFAULT_LANGUAGE = 'en'

# Daily inspirational quotes
DAILY_QUOTES = [
    {
        'en': {
            'quote': 'The smallest act of kindness is worth more than the grandest intention.',
            'author': 'Oscar Wilde'
        },
        'sk': {
            'quote': 'Najmenší prejav láskavosti má väčšiu hodnotu ako najväčší zámer.',
            'author': 'Oscar Wilde'
        }
    },
    {
        'en': {
            'quote': 'Gratitude turns what we have into enough.',
            'author': 'Anonymous'
        },
        'sk': {
            'quote': 'Vďačnosť premení to, čo máme, na dosť.',
            'author': 'Anonymný'
        }
    },
    {
        'en': {
            'quote': 'Joy is not in things; it is in us.',
            'author': 'Richard Wagner'
        },
        'sk': {
            'quote': 'Radosť nie je vo veciach; je v nás.',
            'author': 'Richard Wagner'
        }
    },
    {
        'en': {
            'quote': 'Happiness is not by chance, but by choice.',
            'author': 'Jim Rohn'
        },
        'sk': {
            'quote': 'Šťastie nie je náhoda, ale voľba.',
            'author': 'Jim Rohn'
        }
    },
    {
        'en': {
            'quote': 'The more you praise and celebrate your life, the more there is in life to celebrate.',
            'author': 'Oprah Winfrey'
        },
        'sk': {
            'quote': 'Čím viac chválite a oslavujete svoj život, tým viac je v živote dôvodov na oslavu.',
            'author': 'Oprah Winfrey'
        }
    }
]

# Made with Bob
