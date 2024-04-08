{
    "name": "Mirko Academy groups",
    "summary": "Contacts students, parents and teachers",
    "version": "16.0.1.0.0",
    "category": "Contacts",
    "author": "Manuel Calero, Salvador Gonzalez, Abraham Carrasco, Xtendoo",
    "license": "LGPL-3",
    "application": True,
    "depends": [
        "contacts",
        "mirko_contacts_customization"
    ],
    "data": [
        "views/academy_group_view.xml",
        'views/res_partner_view.xml',
        'security/ir.model.access.csv',
    ],
    "installable": True,
}
