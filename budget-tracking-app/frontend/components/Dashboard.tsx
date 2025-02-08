import React from 'react';
import { useQuery } from 'react-query';
import { fetchBudgets, fetchExpenses } from '../api'; // Assume these API functions are defined

const Dashboard: React.FC = () => {
    const { data: budgets, isLoading: loadingBudgets } = useQuery('budgets', fetchBudgets);
    const { data: expenses, isLoading: loadingExpenses } = useQuery('expenses', fetchExpenses);

    if (loadingBudgets || loadingExpenses) {
        return <div>Loading...</div>;
    }

    const totalBudget = budgets.reduce((acc, budget) => acc + budget.amount, 0);
    const totalExpenses = expenses.reduce((acc, expense) => acc + expense.amount, 0;
    const remainingBalance = totalBudget - totalExpenses;

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold">Dashboard</h1>
            <div className="mt-4">
                <h2 className="text-xl">Total Budget: ${totalBudget}</h2>
                <h2 className="text-xl">Total Expenses: ${totalExpenses}</h2>
                <h2 className="text-xl">Remaining Balance: ${remainingBalance}</h2>
            </div>
            <div className="mt-4">
                <h3 className="text-lg">Budgets</h3>
                <ul>
                    {budgets.map(budget => (
                        <li key={budget.id}>{budget.name}: ${budget.amount}</li>
                    ))}
                </ul>
            </div>
            <div className="mt-4">
                <h3 className="text-lg">Expenses</h3>
                <ul>
                    {expenses.map(expense => (
                        <li key={expense.id}>{expense.category}: ${expense.amount}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Dashboard;