# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Definimos el modelo de datos
class ListaTareas(models.Model):
    # Nombre y descripción del modelo de datos
    _name = 'lista_tareas.lista_tareas'
    _description = 'Lista de tareas'

    # Elementos de cada fila del modelo de datos
    tarea = fields.Char(string='Tarea')
    prioridad = fields.Integer(string='Prioridad')
    urgente = fields.Boolean(
        string='Urgente',
        compute='_value_urgente',
        store=True
    )
    realizada = fields.Boolean(string='Realizada')
    asignado_a = fields.Many2one('res.users', string='Asignado a', required=False, default=lambda self: self.env.user)


    # Este cómputo depende de la variable prioridad
    @api.depends('prioridad')
    def _value_urgente(self):
        # Para cada registro
        for record in self:
            # Si la prioridad es mayor que 10, se considera urgente
            record.urgente = record.prioridad > 10