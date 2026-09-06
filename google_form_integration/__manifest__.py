{
    'name': 'Google Form Integration',

    'version': '15.0.1.0.0',

    'depends': [
        'base',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/google_form_response_views.xml',
    ],

    'installable': True,

    'application': True,
}