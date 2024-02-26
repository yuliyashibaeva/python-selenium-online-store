# Test Cases
## Account creation tests from [the "test_account_creation.py" file](https://github.com/yuliyashibaeva/python-selenium-online-store/blob/main/tests/test_account_creation.py):
### New user account should be created
1. Open the page https://magento.softwaretestingboard.com/customer/account/create/.
2. Fill in all the required fields.
3. Click the "Create an Account" button.<br>

**Expected result:** The success message should be present on the page 
and the user data should be the same as entered in the 2nd step.

### Account creation without a required field should case validation
This test is parametrized. The parameter is one of the field: First Name, Last Name, Email, Password, Confirm Password.
1. Open the page https://magento.softwaretestingboard.com/customer/account/create/.
2. Fill in all the required fields except *<skipped_field>*.
3. Click the "Create an Account" button.<br>

**Expected result:** The skipped field should be marked with red frame 
and have the error message under it.

### Account creation with the existing user email should cause an error
1. Create a new user.
2. Open the page https://magento.softwaretestingboard.com/customer/account/create/.
3. Fill in all the required fields with the same values as in the 1st step.
4. Click the "Create an Account" button.<br>

**Expected result:** There should be an error message saying 
that a user with the same email already exists.

## Shopping cart tests from [the "test_shopping_cart.py" file](https://github.com/yuliyashibaeva/python-selenium-online-store/blob/main/tests/test_shopping_cart.py)
### A product should be added to the cart from the product list page
1. Open the page https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html.
2. Place the cursor on any item and select its size.
3. Select a colour.
4. Click the "Add to Cart" button.

**Expected result:** The success message should be present on the page 
and the quantity of the product in the cart should be equal to 1.

### A product should be added to the cart from the product page
1. Open the page https://magento.softwaretestingboard.com/nadia-elements-shell.html.
2. Select a size.
3. Select a colour.
4. Click the "Add to Cart" button.

**Expected result:** The success message should be present on the page 
and the quantity of the product in the cart should be equal to 1.

### The product data in the cart should be consistent
1. Open the page https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html.
2. Place the cursor on any item and select its size.
3. Select a colour.
4. Click the "Add to Cart" button.
5. Open the cart.

**Expected result:** The product size and colour should be the same 
as selected in the 2nd and 3rd steps.

### The quantity of items in the cart should be updated
1. Open the page https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html.
2. Place the cursor on any item and select its size.
3. Select a colour.
4. Click the "Add to Cart" button.
5. Open the cart.
6. Enter the quantity = 2 in the field "qty" for the just added product.
7. Click the "Update Shopping Cart" button.

**Expected result:** The quantity of the product in the cart should be equal to 2.

### The options of a product in the cart should be updated
1. Open the page https://magento.softwaretestingboard.com/nadia-elements-shell.html.
2. Place the cursor on any item and select its size.
3. Select a colour.
4. Click the "Add to Cart" button.
5. Open the cart.
6. In the line with just added product click the "Edit item parameters" button.
7. Select a size other than the current one.
8. Select a colour other than the current one.
9. Click the "Update Cart" button.

**Expected result:** The success message should be present on the page 
and the product size and colour should be the same as selected 
in the 7th and 8th steps.

### A product should be deleted from the shopping cart
1. Open the page https://magento.softwaretestingboard.com/nadia-elements-shell.html.
2. Place the cursor on any item and select its size.
3. Select a colour.
4. Click the "Add to Cart" button.
5. Open the cart.
6. In the line with just added product click the "Remove item" button.

**Expected result:** There should be a message that the cart is empty and
the cart counter should be absent.