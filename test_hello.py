from hello import say_hello

def test_hello():
    result = say_hello()
    if result == "Hello World":
        print("✅ TEST PASSED!")
        return True
    else:
        print("❌ TEST FAILED!")
        return False

test_hello()
