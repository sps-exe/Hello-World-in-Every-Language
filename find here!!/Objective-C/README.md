# Objective-C

**Year Created:** 1984  
**Creator:** Brad Cox & Tom Love

---

## 💻 Program File: `hello.m`

```
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSLog(@"Hello, World!");
    }
    return 0;
}
```

# ⚙️ Compile & Run

Using clang:
```
clang -fobjc-arc -framework Foundation hello.m -o hello
./hello
```

# 🧠 Fun Fact

Objective-C was created by adding Smalltalk-style object-oriented features to C.
It became the primary language for Apple’s macOS and iOS development before Swift arrived.
The @autoreleasepool and NSLog syntax are part of its unique way of managing memory and output.