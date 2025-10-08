import { invoke } from "@tauri-apps/api/core";
import { useId, useState } from "react";
import reactLogo from "./assets/react.svg";
import "./App.css";

function App() {
	const [greetMsg, setGreetMsg] = useState("");
	const [name, setName] = useState("");

	async function greet() {
		// Learn more about Tauri commands at https://tauri.app/develop/calling-rust/
		setGreetMsg(await invoke("greet", { name }));
	}

	return (
		<main className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
			<h1 className="text-4xl font-bold text-gray-800 mb-8">
				Welcome to Tauri + React
			</h1>

			<div className="flex flex-col md:flex-row gap-4 items-center justify-center">
				<a
					href="https://vite.dev"
					target="_blank"
					className="hover:opacity-80 transition-opacity"
					rel="noopener"
				>
					<img src="/vite.svg" className="w-24 h-24" alt="Vite logo" />
				</a>
				<a
					href="https://tauri.app"
					target="_blank"
					className="hover:opacity-80 transition-opacity"
					rel="noopener"
				>
					<img src="/tauri.svg" className="w-24 h-24" alt="Tauri logo" />
				</a>
				<a
					href="https://reactjs.org"
					target="_blank"
					className="hover:opacity-80 transition-opacity"
					rel="noopener"
				>
					<img
						src={reactLogo}
						className="w-24 h-24 animate-spin-slow"
						alt="React logo"
					/>
				</a>
			</div>
			<p className="text-gray-600 my-6">
				Click on the Tauri, Vite, and React logos to learn more.
			</p>

			<form
				className="row"
				onSubmit={(e) => {
					e.preventDefault();
					greet();
				}}
			>
				<div className="flex flex-col items-center gap-4">
					<div className="flex gap-2">
						<input
							id={useId()}
							onChange={(e) => setName(e.currentTarget.value)}
							placeholder="Enter a name..."
							className="px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
						/>
						<button
							type="button"
							onClick={() => greet()}
							className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
						>
							Greet
						</button>
					</div>
					{greetMsg && (
						<p className="mt-4 p-4 bg-white rounded-lg shadow-md text-gray-800">
							{greetMsg}
						</p>
					)}
				</div>
			</form>
		</main>
	);
}

export default App;
