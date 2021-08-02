onSelectCoffee = (event) => {
const coffee = document.getElementById('edit-coffee').value;
console.log(coffee)
const selectedCoffee = JSON.parse(String(coffee));
document.getElementsByName('coffeeName').value = selectedCoffee.product_name;
} 