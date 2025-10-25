# Haskell

**Year Created:** 1990
**Creator:** A committee (including Simon Peyton Jones, Philip Wadler, etc.)

---

## 💻 Program File: `hello.hs`

```
main :: IO ()
main = putStrLn "Hello, World!"
```

# ⚙️ Compile & Run

```
runhaskell hello.hs
```

# 🧠 Fun Fact

Haskell is a purely functional programming language. This means functions, by default, cannot have "side effects" (like printing to the screen or changing a variable). All side effects are explicitly managed within a special part of the type system, IO, which is why main has the type IO (). It also uses lazy evaluation, meaning expressions are not evaluated until their results are actually needed.