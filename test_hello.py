from calculator import add, subtract

# Test 1
if add(2, 3) == 5:
    print("✅ Test 1 Passed: 2 + 3 = 5")
else:
    print("❌ Test 1 Failed")
    exit(1)

# Test 2
if subtract(5, 3) == 2:
    print("✅ Test 2 Passed: 5 - 3 = 2")
else:
    print("❌ Test 2 Failed")
    exit(1)

print("🎉 All tests passed!")
 
