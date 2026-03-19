
function addSale() {

    fetch("http://127.0.0.1:8000/sales/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            patient: document.getElementById("patient").value,
            amount: document.getElementById("amount").value
        })

    })
        .then(res => res.json())
        .then(data => {
            alert(data.message)
        })

}

function showSales() {

    const respose = fetch("http://127.0.0.1:8000/sales/")
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("result")
            list.innerHTML = ""
            data.forEach(sale => {
                const li = document.createElement("li")
                li.textContent = sale.patient + " - ₹" + sale.amount
                list.appendChild(li)
            })
        })

}

async function addExpense() {

    const item = document.getElementById("item").value
    const expense_amounts = document.getElementById("expense_amount").value

    await fetch("http://127.0.0.1:8000/expenses/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            item: item,
            amount: Number(expense_amounts)
        })
    })

    showEExpenses()
}


async function showExpenses() {

    const response = await fetch("http://127.0.0.1:8000/expenses/")
    const data = await response.json()

    const list = document.getElementById("expenseList")
    list.innerHTML = ""

    data.forEach(exp => {
        const li = document.createElement("li")
        li.textContent = exp.item + " - ₹" + exp.amount
        list.appendChild(li)
    })

}


// Set today's date on frontend
const today = new Date();
const options = { year: 'numeric', month: 'long', day: 'numeric' };
document.getElementById('report-date').innerText = "Date: " + today.toLocaleDateString(undefined, options);

// Fetch report from API
// 
function generateReport() {
    fetch('http://127.0.0.1:8000/reports/reports')
        .then(res => res.json())
        .then(data => {
            document.getElementById('total-sales').innerText = data["Total Sales"];
            document.getElementById('total-expenses').innerText = data["Total Expenses"];
            document.getElementById('profits').innerText = data["Profits"];
        })
        .catch(err => {
            console.error(err);
            document.getElementById('total-sales').innerText = 'Error';
            document.getElementById('total-expenses').innerText = 'Error';
            document.getElementById('profits').innerText = 'Error';
        });
}