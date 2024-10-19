# Oui-Lookup-Generator
使用Python来生成 C++/Rust 的 OUI 查找表程序

[README IN ENGLISH](./README_EN.md)



MAC前6位是厂家标识符，ieee提供了厂家标识符（OUI）及其对应厂家的文本文件：

http://standards-oui.ieee.org/oui/oui.txt

所以我写了一个Python脚本，可以把这个文件转换成C++和Rust程序。

C++ 采用的是switch-case，因为直接 `static const unordered_map`赋初始值太大，会炸。使用 [mapbox](https://github.com/mapbox/eternal) 也会因为初始列表太长导致超过constexpr:step限制。如果有更好的方法，欢迎留言。

Rust采用的是现成的phf库，很快就实现了。



## 用法 

运行 `python main.py rust` 或 `python main.py cpp`后， 该文件会下载[oui.txt](http://standards-oui.ieee.org/oui/oui.txt) 并转换代码，在`output/`文件夹可找到对应代码，即可编译并运行。程序会识别传递的命令行参数，输出对应厂家名称，如果没有则输出`unknown`。

其中Rust需要添加如下依赖。

```toml
[dependencies]
phf = { version = "0.11", features = ["macros"] }
```

## License

The project is released under MIT License.
