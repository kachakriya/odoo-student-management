{
    'name': 'Student Management System',
    'version': '1.0',
    'author': 'Sunfix',
    'summary': 'Student Management',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',

        'views/student_views.xml',
        'views/course_views.xml',
        'views/subject_views.xml',
        'views/menu.xml',

    ],
     'installable': True,
     'application': True,
}