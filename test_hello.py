from hello import say_hello

def test_hello():
    result = say_hello()
    assert result == "Hello World", "Test Failed!"
    print("✅ Test Passed!")

if __name__ == "__main__":
    test_hello()
    print("🎉 All tests passed!")
