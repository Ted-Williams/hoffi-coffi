onSelectCoffee = (event) => {
const coffee = document.getElementById('edit-coffee').value;
const selectedCoffee = JSON.parse(JSON.stringify(coffee));
document.getElementsByName('coffeeName').value = selectedCoffee.product_name;
console.log(selectedCoffee)
} 