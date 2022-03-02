{
    'name': "Odoo Space Mission",

    'summary': "Lancement des missions spatiales",

    'description': """
        Lancement des missions spatiales
    """,

    'author': "Benoit Morel",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [],

    'data': [
        'security/group_odoo_space_mission_security.xml',
        'security/ir.model.access.csv',
        'views/mission.xml',
        'views/spaceship.xml'
    ],

    'demo': [],

    'sequence': '1',

    'installable': True,
    'application': True,
    'auto_install': False,
}
