import React from 'react';

interface BudgetCardProps {
    title: string;
    amount: number;
    spent: number;
    currency: string;
    onEdit: () => void;
    onDelete: () => void;
}

const BudgetCard: React.FC<BudgetCardProps> = ({ title, amount, spent, currency, onEdit, onDelete }) => {
    const remaining = amount - spent;

    return (
        <div className="bg-white shadow-md rounded-lg p-4">
            <h2 className="text-lg font-semibold">{title}</h2>
            <p className="text-gray-600">
                Budget: {currency}{amount.toFixed(2)}
            </p>
            <p className="text-gray-600">
                Spent: {currency}{spent.toFixed(2)}
            </p>
            <p className={`text-${remaining < 0 ? 'red' : 'green'}-600`}>
                Remaining: {currency}{remaining.toFixed(2)}
            </p>
            <div className="flex justify-between mt-4">
                <button onClick={onEdit} className="text-blue-500 hover:underline">Edit</button>
                <button onClick={onDelete} className="text-red-500 hover:underline">Delete</button>
            </div>
        </div>
    );
};

export default BudgetCard;