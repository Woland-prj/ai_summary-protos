# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pyai/pyai.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'pyai/pyai.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fpyai/pyai.proto\x12\x04pyai\x1a\x1egoogle/protobuf/duration.proto\"/\n\x19SpeackerTimestampsRequest\x12\x12\n\naudio_path\x18\x01 \x01(\t\"\xb1\x02\n\x1aSpeackerTimestampsRespones\x12G\n\x0cspeacker_map\x18\x01 \x03(\x0b\x32\x31.pyai.SpeackerTimestampsRespones.SpeackerMapEntry\x12G\n\x0c\x64uration_map\x18\x02 \x03(\x0b\x32\x31.pyai.SpeackerTimestampsRespones.DurationMapEntry\x1a\x32\n\x10SpeackerMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aM\n\x10\x44urationMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x38\x01\"0\n\x1a\x43onvertSpeachToTextRequest\x12\x12\n\naudio_path\x18\x01 \x01(\t\"+\n\x1b\x43onvertSpeachToTextRespones\x12\x0c\n\x04text\x18\x01 \x01(\t\".\n\x19GetFragmentSummaryRequest\x12\x11\n\tbase_text\x18\x01 \x01(\t\"~\n\x15GetFileSummaryRequest\x12\x36\n\x08\x66ragment\x18\x03 \x03(\x0b\x32$.pyai.GetFileSummaryRequest.Fragment\x1a-\n\x08\x46ragment\x12\x10\n\x08speacker\x18\x01 \x01(\t\x12\x0f\n\x07summary\x18\x02 \x01(\t\"*\n\x0fSummaryRespones\x12\x17\n\x0fsummarized_text\x18\x01 \x01(\t2p\n\x12\x44iarizationService\x12Z\n\x15GetSpeackerTimestamps\x12\x1f.pyai.SpeackerTimestampsRequest\x1a .pyai.SpeackerTimestampsRespones2s\n\x15TranscribationService\x12Z\n\x13\x43onvertSpeachToText\x12 .pyai.ConvertSpeachToTextRequest\x1a!.pyai.ConvertSpeachToTextRespones2\xa4\x01\n\x0eSummaryService\x12L\n\x12GetFragmentSummary\x12\x1f.pyai.GetFragmentSummaryRequest\x1a\x15.pyai.SummaryRespones\x12\x44\n\x0eGetFileSummary\x12\x1b.pyai.GetFileSummaryRequest\x1a\x15.pyai.SummaryResponesB\x10Z\x0epyai.v1;pyaiv1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyai.pyai_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\016pyai.v1;pyaiv1'
  _globals['_SPEACKERTIMESTAMPSRESPONES_SPEACKERMAPENTRY']._loaded_options = None
  _globals['_SPEACKERTIMESTAMPSRESPONES_SPEACKERMAPENTRY']._serialized_options = b'8\001'
  _globals['_SPEACKERTIMESTAMPSRESPONES_DURATIONMAPENTRY']._loaded_options = None
  _globals['_SPEACKERTIMESTAMPSRESPONES_DURATIONMAPENTRY']._serialized_options = b'8\001'
  _globals['_SPEACKERTIMESTAMPSREQUEST']._serialized_start=57
  _globals['_SPEACKERTIMESTAMPSREQUEST']._serialized_end=104
  _globals['_SPEACKERTIMESTAMPSRESPONES']._serialized_start=107
  _globals['_SPEACKERTIMESTAMPSRESPONES']._serialized_end=412
  _globals['_SPEACKERTIMESTAMPSRESPONES_SPEACKERMAPENTRY']._serialized_start=283
  _globals['_SPEACKERTIMESTAMPSRESPONES_SPEACKERMAPENTRY']._serialized_end=333
  _globals['_SPEACKERTIMESTAMPSRESPONES_DURATIONMAPENTRY']._serialized_start=335
  _globals['_SPEACKERTIMESTAMPSRESPONES_DURATIONMAPENTRY']._serialized_end=412
  _globals['_CONVERTSPEACHTOTEXTREQUEST']._serialized_start=414
  _globals['_CONVERTSPEACHTOTEXTREQUEST']._serialized_end=462
  _globals['_CONVERTSPEACHTOTEXTRESPONES']._serialized_start=464
  _globals['_CONVERTSPEACHTOTEXTRESPONES']._serialized_end=507
  _globals['_GETFRAGMENTSUMMARYREQUEST']._serialized_start=509
  _globals['_GETFRAGMENTSUMMARYREQUEST']._serialized_end=555
  _globals['_GETFILESUMMARYREQUEST']._serialized_start=557
  _globals['_GETFILESUMMARYREQUEST']._serialized_end=683
  _globals['_GETFILESUMMARYREQUEST_FRAGMENT']._serialized_start=638
  _globals['_GETFILESUMMARYREQUEST_FRAGMENT']._serialized_end=683
  _globals['_SUMMARYRESPONES']._serialized_start=685
  _globals['_SUMMARYRESPONES']._serialized_end=727
  _globals['_DIARIZATIONSERVICE']._serialized_start=729
  _globals['_DIARIZATIONSERVICE']._serialized_end=841
  _globals['_TRANSCRIBATIONSERVICE']._serialized_start=843
  _globals['_TRANSCRIBATIONSERVICE']._serialized_end=958
  _globals['_SUMMARYSERVICE']._serialized_start=961
  _globals['_SUMMARYSERVICE']._serialized_end=1125
# @@protoc_insertion_point(module_scope)
