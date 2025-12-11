# -*- coding: utf-8 -*-

from datetime import date
from multiprocessing import Value
from tokenize import String
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
    fecha_limite = fields.Date(String='Fecha límite para completar la tarea')
    fecha_creacion = fields.Date(String='Fecha en la que se crea la tarea', Value= date.ctime())
    retrasada = fields.Boolean(String = 'Retrasada')

    # Este cómputo depende de la variable prioridad
    @api.depends('prioridad')
    def _value_urgente(self):
        # Para cada registro
        for record in self:
            # Si la prioridad es mayor que 10, se considera urgente
            record.urgente = record.prioridad > 10


    @api.depends('retrasada')
    def _value_retrasada(self):
        #para cada registro
        for record in self:
            #si existe fecha_limite
            if not record.fecha_limite:
                record.retrasada = False
            else:
                # si la fecha actual es mayor que la fecha limite y no testa realizada
                record.retrasada = date.ctime() > record.fecha_limite and not record.realizda