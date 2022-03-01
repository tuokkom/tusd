# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hook.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nhook.proto\x12\x02v2\"5\n\x0bHookRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x18\n\x05\x65vent\x18\x02 \x01(\x0b\x32\t.v2.Event\"K\n\x05\x45vent\x12\x1c\n\x06upload\x18\x01 \x01(\x0b\x32\x0c.v2.FileInfo\x12$\n\x0bhttpRequest\x18\x02 \x01(\x0b\x32\x0f.v2.HTTPRequest\"\xc3\x02\n\x08\x46ileInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x16\n\x0esizeIsDeferred\x18\x03 \x01(\x08\x12\x0e\n\x06offset\x18\x04 \x01(\x03\x12,\n\x08metaData\x18\x05 \x03(\x0b\x32\x1a.v2.FileInfo.MetaDataEntry\x12\x11\n\tisPartial\x18\x06 \x01(\x08\x12\x0f\n\x07isFinal\x18\x07 \x01(\x08\x12\x16\n\x0epartialUploads\x18\x08 \x03(\t\x12*\n\x07storage\x18\t \x03(\x0b\x32\x19.v2.FileInfo.StorageEntry\x1a/\n\rMetaDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a.\n\x0cStorageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9a\x01\n\x0bHTTPRequest\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x12\n\nremoteAddr\x18\x03 \x01(\t\x12+\n\x06header\x18\x04 \x03(\x0b\x32\x1b.v2.HTTPRequest.HeaderEntry\x1a-\n\x0bHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"`\n\x0cHookResponse\x12&\n\x0chttpResponse\x18\x01 \x01(\x0b\x32\x10.v2.HTTPResponse\x12\x14\n\x0crejectUpload\x18\x02 \x01(\x08\x12\x12\n\nstopUpload\x18\x03 \x01(\x08\"\x90\x01\n\x0cHTTPResponse\x12\x12\n\nstatusCode\x18\x01 \x01(\x03\x12.\n\x07headers\x18\x02 \x03(\x0b\x32\x1d.v2.HTTPResponse.HeadersEntry\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32@\n\x0bHookHandler\x12\x31\n\nInvokeHook\x12\x0f.v2.HookRequest\x1a\x10.v2.HookResponse\"\x00\x62\x06proto3')



_HOOKREQUEST = DESCRIPTOR.message_types_by_name['HookRequest']
_EVENT = DESCRIPTOR.message_types_by_name['Event']
_FILEINFO = DESCRIPTOR.message_types_by_name['FileInfo']
_FILEINFO_METADATAENTRY = _FILEINFO.nested_types_by_name['MetaDataEntry']
_FILEINFO_STORAGEENTRY = _FILEINFO.nested_types_by_name['StorageEntry']
_HTTPREQUEST = DESCRIPTOR.message_types_by_name['HTTPRequest']
_HTTPREQUEST_HEADERENTRY = _HTTPREQUEST.nested_types_by_name['HeaderEntry']
_HOOKRESPONSE = DESCRIPTOR.message_types_by_name['HookResponse']
_HTTPRESPONSE = DESCRIPTOR.message_types_by_name['HTTPResponse']
_HTTPRESPONSE_HEADERSENTRY = _HTTPRESPONSE.nested_types_by_name['HeadersEntry']
HookRequest = _reflection.GeneratedProtocolMessageType('HookRequest', (_message.Message,), {
  'DESCRIPTOR' : _HOOKREQUEST,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:v2.HookRequest)
  })
_sym_db.RegisterMessage(HookRequest)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:v2.Event)
  })
_sym_db.RegisterMessage(Event)

FileInfo = _reflection.GeneratedProtocolMessageType('FileInfo', (_message.Message,), {

  'MetaDataEntry' : _reflection.GeneratedProtocolMessageType('MetaDataEntry', (_message.Message,), {
    'DESCRIPTOR' : _FILEINFO_METADATAENTRY,
    '__module__' : 'hook_pb2'
    # @@protoc_insertion_point(class_scope:v2.FileInfo.MetaDataEntry)
    })
  ,

  'StorageEntry' : _reflection.GeneratedProtocolMessageType('StorageEntry', (_message.Message,), {
    'DESCRIPTOR' : _FILEINFO_STORAGEENTRY,
    '__module__' : 'hook_pb2'
    # @@protoc_insertion_point(class_scope:v2.FileInfo.StorageEntry)
    })
  ,
  'DESCRIPTOR' : _FILEINFO,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:v2.FileInfo)
  })
_sym_db.RegisterMessage(FileInfo)
_sym_db.RegisterMessage(FileInfo.MetaDataEntry)
_sym_db.RegisterMessage(FileInfo.StorageEntry)

HTTPRequest = _reflection.GeneratedProtocolMessageType('HTTPRequest', (_message.Message,), {

  'HeaderEntry' : _reflection.GeneratedProtocolMessageType('HeaderEntry', (_message.Message,), {
    'DESCRIPTOR' : _HTTPREQUEST_HEADERENTRY,
    '__module__' : 'hook_pb2'
    # @@protoc_insertion_point(class_scope:v2.HTTPRequest.HeaderEntry)
    })
  ,
  'DESCRIPTOR' : _HTTPREQUEST,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:v2.HTTPRequest)
  })
_sym_db.RegisterMessage(HTTPRequest)
_sym_db.RegisterMessage(HTTPRequest.HeaderEntry)

HookResponse = _reflection.GeneratedProtocolMessageType('HookResponse', (_message.Message,), {
  'DESCRIPTOR' : _HOOKRESPONSE,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:v2.HookResponse)
  })
_sym_db.RegisterMessage(HookResponse)

HTTPResponse = _reflection.GeneratedProtocolMessageType('HTTPResponse', (_message.Message,), {

  'HeadersEntry' : _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _HTTPRESPONSE_HEADERSENTRY,
    '__module__' : 'hook_pb2'
    # @@protoc_insertion_point(class_scope:v2.HTTPResponse.HeadersEntry)
    })
  ,
  'DESCRIPTOR' : _HTTPRESPONSE,
  '__module__' : 'hook_pb2'
  # @@protoc_insertion_point(class_scope:v2.HTTPResponse)
  })
_sym_db.RegisterMessage(HTTPResponse)
_sym_db.RegisterMessage(HTTPResponse.HeadersEntry)

_HOOKHANDLER = DESCRIPTOR.services_by_name['HookHandler']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FILEINFO_METADATAENTRY._options = None
  _FILEINFO_METADATAENTRY._serialized_options = b'8\001'
  _FILEINFO_STORAGEENTRY._options = None
  _FILEINFO_STORAGEENTRY._serialized_options = b'8\001'
  _HTTPREQUEST_HEADERENTRY._options = None
  _HTTPREQUEST_HEADERENTRY._serialized_options = b'8\001'
  _HTTPRESPONSE_HEADERSENTRY._options = None
  _HTTPRESPONSE_HEADERSENTRY._serialized_options = b'8\001'
  _HOOKREQUEST._serialized_start=18
  _HOOKREQUEST._serialized_end=71
  _EVENT._serialized_start=73
  _EVENT._serialized_end=148
  _FILEINFO._serialized_start=151
  _FILEINFO._serialized_end=474
  _FILEINFO_METADATAENTRY._serialized_start=379
  _FILEINFO_METADATAENTRY._serialized_end=426
  _FILEINFO_STORAGEENTRY._serialized_start=428
  _FILEINFO_STORAGEENTRY._serialized_end=474
  _HTTPREQUEST._serialized_start=477
  _HTTPREQUEST._serialized_end=631
  _HTTPREQUEST_HEADERENTRY._serialized_start=586
  _HTTPREQUEST_HEADERENTRY._serialized_end=631
  _HOOKRESPONSE._serialized_start=633
  _HOOKRESPONSE._serialized_end=729
  _HTTPRESPONSE._serialized_start=732
  _HTTPRESPONSE._serialized_end=876
  _HTTPRESPONSE_HEADERSENTRY._serialized_start=830
  _HTTPRESPONSE_HEADERSENTRY._serialized_end=876
  _HOOKHANDLER._serialized_start=878
  _HOOKHANDLER._serialized_end=942
# @@protoc_insertion_point(module_scope)
