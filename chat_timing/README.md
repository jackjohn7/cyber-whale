# Chat Program

This is our Rust-based implementation of a TCP client that converts
delays between messages into binary that is then read into ascii 
values.

# How to Run

Make sure you've installed the Rust toolchain,
[Rustup](https://rustup.rs/).

Rustup comes with Rust's build tool, Cargo.

To run the project, use the following command:
```bash
cargo run --release
```

The `--release` flag specifies that compiler optimizations should
be made. This is important since our program is measuring delays
and inaccuracies in the measurements mean inaccuracies in the 
uncovered covert message.

To compile to a native executable, use the following:
```bash
cargo build --release
```

The resulting binary will be under `target/release/`.

To set the IP of the server, just modify `ip` variable defined on
line 11. `//` is used to comment out a line in Rust. The `ip` is
currently set to point to the IP specified in the program PDF.

To set the delays, modify lines 6 and 7.

Hope you enjoy reading our code.

# Rundown

If you're a fan of simply reading the documentation, here are all
the constructs in use. Names in PascalCase are structs or traits
while names in snake_case are functions.

- [Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html)
- [Instant](https://doc.rust-lang.org/std/time/struct.Instant.html)
- [TcpStream](https://doc.rust-lang.org/std/net/struct.TcpStream.html)
- [Iterator](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [Duration](https://doc.rust-lang.org/std/time/struct.Duration.html)
- [String](https://doc.rust-lang.org/std/string/struct.String.html)
- [from_utf8](https://doc.rust-lang.org/std/str/fn.from_utf8.html)
- [from_str_radix](https://doc.rust-lang.org/std/primitive.u8.html#method.from_str_radix)

If you're unfamiliar with Rust or a more functional-esque style
of programming, this code may seem a bit terse but it's pretty
performant and Rust's compile-time guarantees make it very safe.

First, we allocate a vector (resizable array) to hold all of the
`time::Instant` values that we collect. An instant is a value
marking that exact moment in time. It is guaranteed to be
reliable (i.e. an instant B calculated after instant A, is
guaranteed to be no less than A, barring platform bugs).

Next, a `TcpStream` is created with the `connect` method. This
returns a `io::Result<TcpStream>`. A Result is a sum type that
accounts for a successful case and an unsuccessful case. The
`io::Result<T>` type can return a successful value `T` or an 
erroneous value `io::Error`. The error is not generic for the 
`io::Result<T>`. It simply uses its own error type. The 
`if let` syntax simply allows us to pattern-match on the return
value. The `else` block accounts for a failure in connection.

We first lock the `stdout` guard (a mutex). This is convention,
but not strictly necessary since we are not doing any
concurrency. We acquire stdout to avoid some latency created by
the `println!` macro needing to acquire the lock each time.

We allocate an array of unsigned 8-bit integers called `data` 
for storing the characters sent by the server.

We indefinitely iterate with `loop`. We pattern match on the 
received data from `stream.read` with `match`. We also pass our
array into `read` as a mutable reference so it can be populated
with the characters read. This requires the `Read` trait to be
imported.

If we match on `Ok(0)`, then `0` bytes were read meaning that
the connection was terminated. We match on `Ok(bytes)` when any
other number of bytes are read. Then we push `Instant::now()` into
our vector. Then we write the read characters to stdout. This
requires the `Write` trait to be imported. We then flush the
stdout stream. On an error, simply print it.

At the end, simply print a newline.

Calculate the average between `ONE` and `ZERO`. There tends to be
a bit of premature messaging that occurs since sometimes a 1
character will be delayed *just* under its intended delay
causing it to be potentially seen as a 0 erroneously. Using the 
average value tends to work pretty well. We call this average
`split` because it's the number by which we split the timings
into two distinct groups ('0' and '1').

We use `.windows` method to create 2-element windows into the
structure. Consider array [a, b, c]. the `.windows(2)` method
would yield an iterator on [[a, b], [b, c]]. It allows you to
perform operations on series of adjacent elements. We then `map`
these windows into the `Duration` between the two instant values
converted to milliseconds.

The `collect` method takes an iterator and collects it into one
datastructure. The `iter` method takes a structure and creates
an iterator from it.

We then use `map` to map delays into '0' and '1' values using
the anonymous function (closure) returned from `mapper`. `mapper`
returns a function that dynamically decides how to map the values
appropriately according to the `ONE` and `ZERO` constants set.
These values are collected into a large `String` and the
`as_bytes` method returns the String converted into a slice of
`u8`. We then call `chunks` which is similar to `window` except
there is no overlap. We then convert these slices into `&str`
which is different from `String`
[Explanation](https://blog.logrocket.com/understanding-rust-string-str/).
We format the `&str` to `String` values that are then converted 
to `u8` ascii values using `from_str_radix`. `unwrap` simply states
that we will panic on error case (`None` or `Err`). Then we simply
convert the ascii values to `char` values with `as`. Finally, we
collect the `char` values into a `String`.
I remove any EOF sequence since it shouldn't be printed.

The result of all this computation is assigned to `hidden_msg`. We 
print this to stdout with the `println!` macro.

# Potential Improvements

- [X] CLI argument parsing
- [ ] CLI options allowing user to specify a split and which
value is higher (ONE or ZERO). I think this configuration method
would translate easier to a responsive GUI.
- [ ] A GUI where a user could see a graphical view that would
allow them to filter out ranges of delays similar to EQ would
be sick. It could also allow the user to change their ONE-ZERO or
SPLIT value on the fly and watch the hidden message change in real
time. This could be implemented using Tauri or Egui with relative
ease. This would be enabled with `--gui` flag.
- [ ] A TUI interface enabling some of the features above. Using
keys will alter the values used in decoding the message and would
allow the user to tweak these values on the fly while remaining
in the comfort of their terminal. This could be done with
relative ease using Tauri. Enabled with `--tui` flag.
- [ ] Modes that would allow a user to get delays from other
types of sources (not TCP).
- [ ] Allow the ingestion of predefined delay-data in the format 
JSON or stringified array for analysis.

