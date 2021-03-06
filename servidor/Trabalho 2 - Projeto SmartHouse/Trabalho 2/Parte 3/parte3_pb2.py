# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parte3.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cparte3.proto\x12\tprotoblog\"\xa8\x01\n\x02\x41\x43\x12=\n\x0f\x63onection_state\x18\x01 \x01(\x0e\x32$.protoblog.AC.Device_Conection_State\x12\r\n\x05state\x18\x02 \x01(\t\x12\x13\n\x0btemperature\x18\x03 \x01(\x05\"?\n\x16\x44\x65vice_Conection_State\x12\x0f\n\x0b\x44\x45VICE_IDLE\x10\x00\x12\x14\n\x10\x44\x45VICE_CONNECTED\x10\x01\"\xc2\x01\n\x10IrrigationSystem\x12K\n\x0f\x63onection_state\x18\x01 \x01(\x0e\x32\x32.protoblog.IrrigationSystem.Device_Conection_State\x12\r\n\x05state\x18\x02 \x01(\t\x12\x11\n\tintensity\x18\x03 \x01(\x05\"?\n\x16\x44\x65vice_Conection_State\x12\x0f\n\x0b\x44\x45VICE_IDLE\x10\x00\x12\x14\n\x10\x44\x45VICE_CONNECTED\x10\x01\"\xac\x01\n\x04lamp\x12\x13\n\x0b\x64\x65vice_name\x18\x01 \x01(\t\x12?\n\x0f\x63onection_state\x18\x02 \x01(\x0e\x32&.protoblog.lamp.Device_Conection_State\x12\r\n\x05state\x18\x03 \x01(\t\"?\n\x16\x44\x65vice_Conection_State\x12\x0f\n\x0b\x44\x45VICE_IDLE\x10\x00\x12\x14\n\x10\x44\x45VICE_CONNECTED\x10\x01\"\x16\n\x07MESSAGE\x12\x0b\n\x03msg\x18\x06 \x01(\t*?\n\x16\x44\x65vice_Conection_State\x12\x0f\n\x0b\x44\x45VICE_IDLE\x10\x00\x12\x14\n\x10\x44\x45VICE_CONNECTED\x10\x01\x62\x06proto3')

_DEVICE_CONECTION_STATE = DESCRIPTOR.enum_types_by_name['Device_Conection_State']
Device_Conection_State = enum_type_wrapper.EnumTypeWrapper(_DEVICE_CONECTION_STATE)
DEVICE_IDLE = 0
DEVICE_CONNECTED = 1


_AC = DESCRIPTOR.message_types_by_name['AC']
_IRRIGATIONSYSTEM = DESCRIPTOR.message_types_by_name['IrrigationSystem']
_LAMP = DESCRIPTOR.message_types_by_name['lamp']
_MESSAGE = DESCRIPTOR.message_types_by_name['MESSAGE']
_AC_DEVICE_CONECTION_STATE = _AC.enum_types_by_name['Device_Conection_State']
_IRRIGATIONSYSTEM_DEVICE_CONECTION_STATE = _IRRIGATIONSYSTEM.enum_types_by_name['Device_Conection_State']
_LAMP_DEVICE_CONECTION_STATE = _LAMP.enum_types_by_name['Device_Conection_State']
AC = _reflection.GeneratedProtocolMessageType('AC', (_message.Message,), {
  'DESCRIPTOR' : _AC,
  '__module__' : 'parte3_pb2'
  # @@protoc_insertion_point(class_scope:protoblog.AC)
  })
_sym_db.RegisterMessage(AC)

IrrigationSystem = _reflection.GeneratedProtocolMessageType('IrrigationSystem', (_message.Message,), {
  'DESCRIPTOR' : _IRRIGATIONSYSTEM,
  '__module__' : 'parte3_pb2'
  # @@protoc_insertion_point(class_scope:protoblog.IrrigationSystem)
  })
_sym_db.RegisterMessage(IrrigationSystem)

lamp = _reflection.GeneratedProtocolMessageType('lamp', (_message.Message,), {
  'DESCRIPTOR' : _LAMP,
  '__module__' : 'parte3_pb2'
  # @@protoc_insertion_point(class_scope:protoblog.lamp)
  })
_sym_db.RegisterMessage(lamp)

MESSAGE = _reflection.GeneratedProtocolMessageType('MESSAGE', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'parte3_pb2'
  # @@protoc_insertion_point(class_scope:protoblog.MESSAGE)
  })
_sym_db.RegisterMessage(MESSAGE)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DEVICE_CONECTION_STATE._serialized_start=133
  _DEVICE_CONECTION_STATE._serialized_end=196
  _AC._serialized_start=28
  _AC._serialized_end=196
  _AC_DEVICE_CONECTION_STATE._serialized_start=133
  _AC_DEVICE_CONECTION_STATE._serialized_end=196
  _IRRIGATIONSYSTEM._serialized_start=199
  _IRRIGATIONSYSTEM._serialized_end=393
  _IRRIGATIONSYSTEM_DEVICE_CONECTION_STATE._serialized_start=133
  _IRRIGATIONSYSTEM_DEVICE_CONECTION_STATE._serialized_end=196
  _LAMP._serialized_start=396
  _LAMP._serialized_end=568
  _LAMP_DEVICE_CONECTION_STATE._serialized_start=133
  _LAMP_DEVICE_CONECTION_STATE._serialized_end=196
  _MESSAGE._serialized_start=570
  _MESSAGE._serialized_end=592
# @@protoc_insertion_point(module_scope)
