# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyai import pyai_pb2 as pyai_dot_pyai__pb2

GRPC_GENERATED_VERSION = '1.69.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in pyai/pyai_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class DiarizationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSpeackerTimestamps = channel.unary_unary(
                '/pyai.DiarizationService/GetSpeackerTimestamps',
                request_serializer=pyai_dot_pyai__pb2.SpeackerTimestampsRequest.SerializeToString,
                response_deserializer=pyai_dot_pyai__pb2.SpeackerTimestampsRespones.FromString,
                _registered_method=True)


class DiarizationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSpeackerTimestamps(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DiarizationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSpeackerTimestamps': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSpeackerTimestamps,
                    request_deserializer=pyai_dot_pyai__pb2.SpeackerTimestampsRequest.FromString,
                    response_serializer=pyai_dot_pyai__pb2.SpeackerTimestampsRespones.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pyai.DiarizationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('pyai.DiarizationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DiarizationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSpeackerTimestamps(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pyai.DiarizationService/GetSpeackerTimestamps',
            pyai_dot_pyai__pb2.SpeackerTimestampsRequest.SerializeToString,
            pyai_dot_pyai__pb2.SpeackerTimestampsRespones.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class TranscribationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConvertSpeachToText = channel.unary_unary(
                '/pyai.TranscribationService/ConvertSpeachToText',
                request_serializer=pyai_dot_pyai__pb2.ConvertSpeachToTextRequest.SerializeToString,
                response_deserializer=pyai_dot_pyai__pb2.ConvertSpeachToTextRespones.FromString,
                _registered_method=True)


class TranscribationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ConvertSpeachToText(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TranscribationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ConvertSpeachToText': grpc.unary_unary_rpc_method_handler(
                    servicer.ConvertSpeachToText,
                    request_deserializer=pyai_dot_pyai__pb2.ConvertSpeachToTextRequest.FromString,
                    response_serializer=pyai_dot_pyai__pb2.ConvertSpeachToTextRespones.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pyai.TranscribationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('pyai.TranscribationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TranscribationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ConvertSpeachToText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pyai.TranscribationService/ConvertSpeachToText',
            pyai_dot_pyai__pb2.ConvertSpeachToTextRequest.SerializeToString,
            pyai_dot_pyai__pb2.ConvertSpeachToTextRespones.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class SummaryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFragmentSummary = channel.unary_unary(
                '/pyai.SummaryService/GetFragmentSummary',
                request_serializer=pyai_dot_pyai__pb2.GetFragmentSummaryRequest.SerializeToString,
                response_deserializer=pyai_dot_pyai__pb2.SummaryRespones.FromString,
                _registered_method=True)
        self.GetFileSummary = channel.unary_unary(
                '/pyai.SummaryService/GetFileSummary',
                request_serializer=pyai_dot_pyai__pb2.GetFileSummaryRequest.SerializeToString,
                response_deserializer=pyai_dot_pyai__pb2.SummaryRespones.FromString,
                _registered_method=True)


class SummaryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetFragmentSummary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFileSummary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SummaryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetFragmentSummary': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFragmentSummary,
                    request_deserializer=pyai_dot_pyai__pb2.GetFragmentSummaryRequest.FromString,
                    response_serializer=pyai_dot_pyai__pb2.SummaryRespones.SerializeToString,
            ),
            'GetFileSummary': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFileSummary,
                    request_deserializer=pyai_dot_pyai__pb2.GetFileSummaryRequest.FromString,
                    response_serializer=pyai_dot_pyai__pb2.SummaryRespones.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pyai.SummaryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('pyai.SummaryService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SummaryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetFragmentSummary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pyai.SummaryService/GetFragmentSummary',
            pyai_dot_pyai__pb2.GetFragmentSummaryRequest.SerializeToString,
            pyai_dot_pyai__pb2.SummaryRespones.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetFileSummary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pyai.SummaryService/GetFileSummary',
            pyai_dot_pyai__pb2.GetFileSummaryRequest.SerializeToString,
            pyai_dot_pyai__pb2.SummaryRespones.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
