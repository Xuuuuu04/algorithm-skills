<div align="center">
<h1>grpc-cj</h1>
</div>
<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v0.0.1-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.0-brightgreen" style="display: inline-block;" />
</p>



## <img alt="" src="./doc/readme-image/readme-icon-introduction.png" style="display: inline-block;" width=3%/> 1 介绍

grpc-cj旨在为Cangjie语言提供了完整的 gRPC 协议支持，使开发者能够基于该语言轻松构建高性能、跨平台的分布式微服务系统。API与grpc-java保持一致，底层使用Cangjie语言的net.http库，集成 gRPC 的核心通信机制（如 HTTP/2 传输、Protocol Buffers 序列化、流式 RPC 等），开发者可直接使用Cangjie编写服务端与客户端，实现与 Java、Go、Python 等主流语言的无缝互操作。

### 1.1 项目特性


## <img alt="" src="./doc/readme-image/readme-icon-framework.png" style="display: inline-block;" width=3%/> 2 架构
<img alt="" src="./doc/grpc.png" style="display: block;" width=50%/>

### 2.1 项目结构

### 2.2 接口说明

## <img alt="" src="./doc/readme-image/readme-icon-compile.png" style="display: inline-block;" width=3%/> 3 使用说明

### 3.1 编译构建（Win/Linux/Mac）

在项目的cjpm.toml文件添加以下配置后，再执行cjpm update，即可在项目中引入grpc-cj（需要额外设置环境变量CANGJIE_STDX，值为stdx的路径）

例如：

```tex
C:\Windows\System32>echo %CANGJIE_STDX%
C:\Users\30247\Desktop\Cangjie\Cangjie-1.0.0\cangjie-stdx-windows-x64-1.0.1.1\windows_x86_64_llvm\dynamic\stdx
```

```toml
[dependencies]
  grpc = {git = "https://gitcode.com/Yesokim/grpc-cj.git", branch="master"}
```

### 3.2 使用示例

```protobuf
syntax = "proto3";

message HelloRequest{
    string name = 1;
}

message HelloResponse{
    string result = 1;
}

service HelloService{
    rpc hello(HelloRequest) returns (HelloResponse){}
}
```

以上面的proto文件为例，使用[protoc-plugin-cj](https://gitcode.com/Yesokim/protoc-plugin-cj)插件生成Cangjie代码后引入到项目中

#### 3.2.1 服务端示例

```cangjie
import std.io.*
import std.fs.*
import net.tls.*
import crypto.x509.*
import grpc.server.*
import grpc.common.*

main() {
        let cert = String.fromUtf8(readToEnd(File("./server.crt", Read)))
        let key = String.fromUtf8(readToEnd(File("./server.key", Read)))
        var tlsConfig = TlsServerConfig(X509Certificate.decodeFromPem(cert), PrivateKey.decodeFromPem(key))
        tlsConfig.supportedAlpnProtocols = ["h2"]
        let channel = ServerChannelBuilder().tlsConfig(tlsConfig).build()
        channel.addService(HelloServiceImpl())
        channel.start()
}

public class HelloServiceImpl <: HelloServiceImplBase {

    public func hello(request: HelloRequest, observer: StreamObserver<HelloResponse>): Unit {
        println("request: ${request.name}")
        let response = HelloResponse.newBuilder().setResult("hello ${request.name.getOrThrow()}").build()
        observer.onNext(response)
        observer.onCompleted()
    }

}
```

#### 3.2.2 客户端示例

```cangjie
import grpc.client.*

main() {
    let channel = ClientChannelBuilder().address("127.0.0.1").port(9000).build()
    let request = HelloRequest.newBuilder().setName("Yesokim").build()
    let helloServiceStub = HelloServiceGrpc.newBlockingStub(channel)
    let response = helloServiceStub.hello(request)
}
```

#### 3.2.3 客户端拦截器

```cangjie
main() {
	let channel = ClientChannelBuilder()
					.address("127.0.0.1")
					.port(9000)
					.intercept(AuthenticationInterceptor())//注册拦截器
					.build()
}
//实现客户端拦截器
public class AuthenticationIntecetptor <: ClientInterceptor {

    public func interceptCall<Req, Res>(method: MethodDescriptor<Req, Res>, channel: ClientChannel): ClientCall<Req, Res> {
        return AuthenticationClientCall(channel.newCall(method))
    }

}
//拦截ClientCall
public class AuthenticationClientCall<Req, Res> <: DelegatedClientCall<Req, Res> {

    public init(delegate: ClientCall<Req, Res>) {
        super(delegate)
    }

    public func start(listener: ClientCallListener<Res>, metadata: Metadata): Unit {
        metadata.headers.add("Authorization", "token")
        super.start(listener, metadata)
    }
}
```

#### 3.2.4 服务端拦截器

```cangjie
main() {
	let cert = String.fromUtf8(readToEnd(File("./server.crt", Read)))
    let key = String.fromUtf8(readToEnd(File("./server.key", Read)))
    var tlsConfig = TlsServerConfig(X509Certificate.decodeFromPem(cert), PrivateKey.decodeFromPem(key))
    tlsConfig.supportedAlpnProtocols = ["h2"]
    let channel = ServerChannelBuilder()
    					.tlsConfig(tlsConfig)
    					.intercept(AuthenticationIntecetptor())//注册拦截器
    					.build()
}

//实现服务端拦截器
public class AuthenticationIntecetptor <: ServerInterceptor {

     public func interceptCall<Req, Res>(call: ServerCall<Req, Res>, metadata: Metadata, callHandler: ServerCallHandler<Req, Res>): ServerCallListener<Req> {
        return AuthenticationServerCallHandler<Req, Res>(callHandler).startCall(call, metadata)
    }

}

//拦截ServerCall
public class AuthenticationServerCallHandler<Req, Res> <: ServerCallHandler<Req, Res> {

    private let delegate: ServerCallHandler<Req, Res>

    public init(delegate: ServerCallHandler<Req, Res>) {
        this.delegate = delegate
    }

    public func startCall(call: ServerCall<Req, Res>, metadata: Metadata): ServerCallListener<Req> {
        let auth = metadata.headers.getFirst("authorization").getOrThrow()
        delegate.startCall(call, metadata)
    }

}
```



## <img alt="" src="./doc/readme-image/readme-icon-contribute.png" style="display: inline-block;" width=3%/>4 参与贡献

本项目由Yesokim实现并维护。技术支持和意见反馈请提Issue。

本项目基于 Apache License 2.0，欢迎给我们提交PR，欢迎参与任何形式的贡献。

本项目commiter：[@Yesokim](https://gitcode.com/weixin_64400442)
