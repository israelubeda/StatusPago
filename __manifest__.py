##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2023 Israel Ubeda Bravo
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Agregando Status Pago',
    'version': '14.0.1.0.0',
    'author': 'Israel Ubeda Bravo',
    'maintainer': 'Israel Ubeda Bravo',
    'website': 'https://github.com/israelubeda',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'Agregando status de Pago a la ordenes de Venta',
    'depends': ['sale'],
    'data': [
        #'security/ir.model.access.csv',
        #'security/groups.xml',
        #'views/assets.xml',
        'views/sale.xml',

    ],
    'qweb': [
        #'static/src/xml/Dashboard.xml',
        #'static/src/xml/SaleDashboard.xml',
    ],
    'images': ['static/description/banner.jpg'],
}
