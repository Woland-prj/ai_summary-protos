{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    protobuf
    go
    python3
    python3Packages.grpcio-tools
  ];

  shellHook = ''
    # Добавляем GOPATH/bin в PATH
    export PATH="$PATH:$(go env GOPATH)/bin"

    # Генерация Go-кода из .proto
    mkdir -p gen/go
    protoc -I proto proto/pyai/pyai.proto \
      --go_out=./gen/go --go_opt=paths=source_relative \
      --go-grpc_out=./gen/go --go-grpc_opt=paths=source_relative

    # Генерация Python-кода из .proto
    mkdir -p gen/python
    python -m grpc_tools.protoc -Iproto \
      --python_out=./gen/python \
      --grpc_python_out=./gen/python \
      proto/pyai/pyai.proto
  '';
}
