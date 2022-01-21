# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exaustor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='exaustor.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x65xaustor.proto\" \n\x0eStatusExaustor\x12\x0e\n\x06status\x18\x01 \x01(\x02\x32w\n\x08\x45xaustor\x12\x33\n\rligarExaustor\x12\x0f.StatusExaustor\x1a\x0f.StatusExaustor\"\x00\x12\x36\n\x10\x64\x65sligarExaustor\x12\x0f.StatusExaustor\x1a\x0f.StatusExaustor\"\x00\x62\x06proto3'
)




_STATUSEXAUSTOR = _descriptor.Descriptor(
  name='StatusExaustor',
  full_name='StatusExaustor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='StatusExaustor.status', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=50,
)

DESCRIPTOR.message_types_by_name['StatusExaustor'] = _STATUSEXAUSTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatusExaustor = _reflection.GeneratedProtocolMessageType('StatusExaustor', (_message.Message,), {
  'DESCRIPTOR' : _STATUSEXAUSTOR,
  '__module__' : 'exaustor_pb2'
  # @@protoc_insertion_point(class_scope:StatusExaustor)
  })
_sym_db.RegisterMessage(StatusExaustor)



_EXAUSTOR = _descriptor.ServiceDescriptor(
  name='Exaustor',
  full_name='Exaustor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=52,
  serialized_end=171,
  methods=[
  _descriptor.MethodDescriptor(
    name='ligarExaustor',
    full_name='Exaustor.ligarExaustor',
    index=0,
    containing_service=None,
    input_type=_STATUSEXAUSTOR,
    output_type=_STATUSEXAUSTOR,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='desligarExaustor',
    full_name='Exaustor.desligarExaustor',
    index=1,
    containing_service=None,
    input_type=_STATUSEXAUSTOR,
    output_type=_STATUSEXAUSTOR,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXAUSTOR)

DESCRIPTOR.services_by_name['Exaustor'] = _EXAUSTOR

# @@protoc_insertion_point(module_scope)
