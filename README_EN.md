# Oui-Lookup-Generator

Using python to generate C++/Rust OUI lookup program.



The first 6 bits of MAC are the manufacturer identifier, and IEEE provides the manufacturer identifier (OUI) and its corresponding manufacturer in this text file:

http://standards-oui.ieee.org/oui/oui.txt

So I wrote a Python script that can translate this file into C++ and Rust programs.

C++ uses switch-case because directly assigning `static const unordered_map` with an initial value that is too large can cause problems. Using [mapbox](https://github.com/mapbox/eternal) may also exceed the `constexpr:step` limit due to the initial list being too long. If there is a better way, please feel free to leave a message.

Rust used the phf library and easily applied.



## Usage

Run `python main.py rust` or `python main.py cpp`, it will download [oui.txt](http://standards-oui.ieee.org/oui/oui.txt) and translate the code, output them to `output/` folder. Rust needs this dependency:

```toml
[dependencies]
phf = { version = "0.11", features = ["macros"] }
```

## License

The project is released under MIT License.