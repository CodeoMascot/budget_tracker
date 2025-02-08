import React from 'react';
import Head from 'next/head';
import Navbar from '../components/Navbar';

const Home: React.FC = () => {
    return (
        <div>
            <Head>
                <title>Budget Tracking App</title>
                <meta name="description" content="Track your expenses and manage your budget effectively." />
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <Navbar />
            <main className="flex flex-col items-center justify-center min-h-screen py-2">
                <h1 className="text-4xl font-bold">Welcome to Budget Tracking App</h1>
                <p className="mt-4 text-lg">Manage your expenses and budgets with ease.</p>
            </main>
        </div>
    );
};

export default Home;