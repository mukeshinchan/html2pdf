// 1. Grab the save-el paragrah and store it in a variable called saveEl
let total = 0 
let countEl = document.getElementById("count-el")
let count = 0
let total2 = "{0"

function increment() {
    count += 1
    countEl.innerText = count
}

function decrement() {
    count = count - 1
    countEl.innerText = count
}

function save() {
    // 2. Create a variable that contains both the count and the dash separator, i.e. "12 - "
    // 3. Render the variable in the saveEl using innerText
    // NB: Make sure to not delete the existing content of the paragraph
    console.log(count)
    total = count + total
    document.getElementById("totalp").innerHTML = total
    total2 = total2 +"} / {"+ count
    document.getElementById("pre1").innerHTML = total2
    count = 0
    countEl.innerText = count
}


