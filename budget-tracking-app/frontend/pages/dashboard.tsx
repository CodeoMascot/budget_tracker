import React from 'react';
import { useQuery } from 'react-query';
import { fetchDashboardData } from '../api/dashboardApi';
import BudgetCard from '../components/BudgetCard';
import ExpenseForm from '../components/ExpenseForm';

const Dashboard: React.FC = () => {
    const { data, isLoading, error } = useQuery('dashboardData', fetchDashboardData);

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>Error loading dashboard data</div>;

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold">Dashboard</h1>
            <div className="mt-4">
                <h2 className="text-xl">Budgets</h2>
                {data.budgets.map(budget => (
                    <BudgetCard key={budget.id} budget={budget} />
                ))}
            </div>
            <div className="mt-4">
                <h2 className="text-xl">Add Expense</h2>
                <ExpenseForm />
            </div>
        </div>
    );
};

export default Dashboard;