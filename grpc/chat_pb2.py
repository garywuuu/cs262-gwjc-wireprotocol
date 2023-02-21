# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nchat.proto\x12\x04grpc\"\x07\n\x05\x45mpty\"?\n\x07Message\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x11\n\trecipient\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"!\n\rSignupRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"-\n\x0bSignupReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\" \n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\",\n\nLoginReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"!\n\rLogoutRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"-\n\x0bLogoutReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t2\xf6\x01\n\nChatServer\x12*\n\nChatStream\x12\x0b.grpc.Empty\x1a\r.grpc.Message0\x01\x12)\n\x0bSendMessage\x12\r.grpc.Message\x1a\x0b.grpc.Empty\x12\x30\n\x06Signup\x12\x13.grpc.SignupRequest\x1a\x11.grpc.SignupReply\x12-\n\x05Login\x12\x12.grpc.LoginRequest\x1a\x10.grpc.LoginReply\x12\x30\n\x06Logout\x12\x13.grpc.LogoutRequest\x1a\x11.grpc.LogoutReplyb\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='grpc.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_end=27,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='grpc.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='grpc.Message.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='grpc.Message.recipient', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc.Message.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=29,
  serialized_end=92,
)


_SIGNUPREQUEST = _descriptor.Descriptor(
  name='SignupRequest',
  full_name='grpc.SignupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='grpc.SignupRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=94,
  serialized_end=127,
)


_SIGNUPREPLY = _descriptor.Descriptor(
  name='SignupReply',
  full_name='grpc.SignupReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='grpc.SignupReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='grpc.SignupReply.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=129,
  serialized_end=174,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='grpc.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='grpc.LoginRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=176,
  serialized_end=208,
)


_LOGINREPLY = _descriptor.Descriptor(
  name='LoginReply',
  full_name='grpc.LoginReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='grpc.LoginReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='grpc.LoginReply.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=210,
  serialized_end=254,
)


_LOGOUTREQUEST = _descriptor.Descriptor(
  name='LogoutRequest',
  full_name='grpc.LogoutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='grpc.LogoutRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=256,
  serialized_end=289,
)


_LOGOUTREPLY = _descriptor.Descriptor(
  name='LogoutReply',
  full_name='grpc.LogoutReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='grpc.LogoutReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='grpc.LogoutReply.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=291,
  serialized_end=336,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['SignupRequest'] = _SIGNUPREQUEST
DESCRIPTOR.message_types_by_name['SignupReply'] = _SIGNUPREPLY
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginReply'] = _LOGINREPLY
DESCRIPTOR.message_types_by_name['LogoutRequest'] = _LOGOUTREQUEST
DESCRIPTOR.message_types_by_name['LogoutReply'] = _LOGOUTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Empty)
  })
_sym_db.RegisterMessage(Empty)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Message)
  })
_sym_db.RegisterMessage(Message)

SignupRequest = _reflection.GeneratedProtocolMessageType('SignupRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.SignupRequest)
  })
_sym_db.RegisterMessage(SignupRequest)

SignupReply = _reflection.GeneratedProtocolMessageType('SignupReply', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPREPLY,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.SignupReply)
  })
_sym_db.RegisterMessage(SignupReply)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

LoginReply = _reflection.GeneratedProtocolMessageType('LoginReply', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREPLY,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.LoginReply)
  })
_sym_db.RegisterMessage(LoginReply)

LogoutRequest = _reflection.GeneratedProtocolMessageType('LogoutRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUTREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.LogoutRequest)
  })
_sym_db.RegisterMessage(LogoutRequest)

LogoutReply = _reflection.GeneratedProtocolMessageType('LogoutReply', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUTREPLY,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.LogoutReply)
  })
_sym_db.RegisterMessage(LogoutReply)



_CHATSERVER = _descriptor.ServiceDescriptor(
  name='ChatServer',
  full_name='grpc.ChatServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=339,
  serialized_end=585,
  methods=[
  _descriptor.MethodDescriptor(
    name='ChatStream',
    full_name='grpc.ChatServer.ChatStream',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='grpc.ChatServer.SendMessage',
    index=1,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Signup',
    full_name='grpc.ChatServer.Signup',
    index=2,
    containing_service=None,
    input_type=_SIGNUPREQUEST,
    output_type=_SIGNUPREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='grpc.ChatServer.Login',
    index=3,
    containing_service=None,
    input_type=_LOGINREQUEST,
    output_type=_LOGINREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Logout',
    full_name='grpc.ChatServer.Logout',
    index=4,
    containing_service=None,
    input_type=_LOGOUTREQUEST,
    output_type=_LOGOUTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHATSERVER)

DESCRIPTOR.services_by_name['ChatServer'] = _CHATSERVER

# @@protoc_insertion_point(module_scope)
