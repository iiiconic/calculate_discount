def calculate_discount (price, discount_percent):
  if discount_percent >= 20:
    discounted_price = price * (discount_percent/100);
    final_price = price - discounted_price;
    return final_price
  else:
    return price;

original_price = float(input("Enter price: "));
discount = float(input("Enter discount: "));

final_price = calculate_discount(original_price, discount);

if final_price != original_price:
  print("Discount Price: ", final_price);
else:
  print("No Discount Applied: ", final_price);