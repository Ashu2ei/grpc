# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x63\x61lculator.proto\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x02\x32.\n\nCalculator\x12 \n\nSquareRoot\x12\x07.Number\x1a\x07.Number\"\x00\x62\x06proto3'
)




_NUMBER = _descriptor.Descriptor(
  name='Number',
  full_name='Number',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Number.value', index=0,
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
  serialized_start=20,
  serialized_end=43,
)

DESCRIPTOR.message_types_by_name['Number'] = _NUMBER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:Number)
  })
_sym_db.RegisterMessage(Number)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=45,
  serialized_end=91,
  methods=[
  _descriptor.MethodDescriptor(
    name='SquareRoot',
    full_name='Calculator.SquareRoot',
    index=0,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_NUMBER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
