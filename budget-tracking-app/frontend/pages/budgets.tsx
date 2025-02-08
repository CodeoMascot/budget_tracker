import React, { useEffect, useState } from 'react';
import axios from 'axios';
import BudgetCard from '../components/BudgetCard';

const BudgetsPage = () => {
  const [budgets, setBudgets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchBudgets = async () => {
      try {
        const response = await axios.get('/api/budgets');
        setBudgets(response.data);
      } catch (err) {
        setError('Failed to fetch budgets');
      } finally {
        setLoading(false);
      }
    };

    fetchBudgets();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Budgets</h1>
      <div className="grid grid-cols-1 gap-4">
        {budgets.map((budget) => (
          <BudgetCard key={budget.id} budget={budget} />
        ))}
      </div>
    </div>
  );
};

export default BudgetsPage;