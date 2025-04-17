import React, { useState, useEffect } from "react";
import BarContainer from "../../components/BarContainer/BarContainer";

const Home = () => {
    const [stages, setStages] = useState([]);
    const [currentStep, setCurrentStep] = useState(0);
    const [isPlaying, setIsPlaying] = useState(false);
    const [speed, setSpeed] = useState(100);
    const [count, setCount] = useState(100);
    const [customInput, setCustomInput] = useState("");
    const [algorithm, setAlgorithm] = useState("insertion");

    const generateRandomData = (length) => {
        return Array.from({ length }, () => Math.floor(Math.random() * 100) + 1);
    };

    const fetchStages = async (data) => {
        try {
            const response = await fetch("http://localhost:5000/sort", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    input_data: data,
                    algorithms: algorithm,
                }),
            });
            const result = await response.json();
            setStages(result.stages || []);
            setCurrentStep(0);
        } catch (error) {
            console.error("Error fetching sorting stages:", error);
        }
    };

    useEffect(() => {
        const randomData = generateRandomData(count);
        fetchStages(randomData);
    }, [count, algorithm]);

    useEffect(() => {
        if (stages.length === 0 || !isPlaying) return;

        const interval = setInterval(() => {
            setCurrentStep((prevStep) => {
                if (prevStep >= stages.length - 1) {
                    clearInterval(interval);
                    setIsPlaying(false);
                    return prevStep;
                }
                return prevStep + 1;
            });
        }, speed);

        return () => clearInterval(interval);
    }, [stages, isPlaying, speed]);

    const handlePlayPause = () => {
        setIsPlaying(!isPlaying);
    };

    const handleStepForward = () => {
        setCurrentStep((prevStep) => Math.min(prevStep + 1, stages.length - 1));
    };

    const handleStepBackward = () => {
        setCurrentStep((prevStep) => Math.max(prevStep - 1, 0));
    };

    const handleReset = () => {
        setCurrentStep(0);
        setIsPlaying(false);
    };

    const handleSpeedChange = (event) => {
        setSpeed(event.target.value);
    };

    const handleCountChange = (event) => {
        setCount(parseInt(event.target.value));
    };

    const handleCustomInputChange = (event) => {
        setCustomInput(event.target.value);
    };

    const handleCustomInputSubmit = () => {
        const parsed = customInput
            .split(",")
            .map((n) => parseInt(n.trim()))
            .filter((n) => !isNaN(n));
        if (parsed.length > 0) {
            setCount(parsed.length);
            fetchStages(parsed);
        }
    };

    const handleRandomize = () => {
        const randomData = generateRandomData(count);
        fetchStages(randomData);
    };

    const handleShuffleOrder = () => {
        const currentData = stages[currentStep] || [];
        const shuffled = [...currentData].sort(() => Math.random() - 0.5);
        fetchStages(shuffled);
    };

    const handleAlgorithmChange = (event) => {
        setAlgorithm(event.target.value);
    };

    return (
        <div
            style={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
                height: "100vh",
                fontFamily: "inherit",
            }}
        >
            <BarContainer data={stages[currentStep] || []} height="75%" width="75%" />
            <div
                style={{
                    marginTop: "20px",
                    display: "flex",
                    alignItems: "center",
                    gap: "10px",
                    flexWrap: "wrap",
                    justifyContent: "center",
                    fontFamily: "inherit",
                }}
            >
                <button onClick={handleReset} style={{ margin: "5px" }}>Reset</button>
                <button onClick={handleStepBackward} style={{ margin: "5px" }}>Step Backward</button>
                <button onClick={handlePlayPause} style={{ margin: "5px" }}>
                    {isPlaying ? "Pause" : "Play"}
                </button>
                <button onClick={handleStepForward} style={{ margin: "5px" }}>Step Forward</button>

                <label htmlFor="speedSlider" style={{ marginLeft: "15px" }}>Speed:</label>
                <input
                    id="speedSlider"
                    type="range"
                    min="10"
                    max="2000"
                    step="10"
                    value={speed}
                    onChange={handleSpeedChange}
                />
                <span style={{ minWidth: "50px", textAlign: "right" }}>{speed} ms</span>

                <label htmlFor="countSlider" style={{ marginLeft: "20px" }}>Elements:</label>
                <input
                    id="countSlider"
                    type="range"
                    min="10"
                    max="200"
                    step="1"
                    value={count}
                    onChange={handleCountChange}
                />
                <span style={{ minWidth: "40px", textAlign: "right" }}>{count}</span>

                <label htmlFor="algorithmSelect">Algorithm:</label>
                <select
                    id="algorithmSelect"
                    value={algorithm}
                    onChange={handleAlgorithmChange}
                    style={{ padding: "5px" }}
                >
                    <option value="insertion">Insertion Sort</option>
                    <option value="bubble">Bubble Sort</option>
                    <option value="merge">Merge Sort</option>
                    <option value="quick">Quick Sort</option>
                </select>

                <input
                    type="text"
                    placeholder="e.g. 12, 5, 33, 7"
                    value={customInput}
                    onChange={handleCustomInputChange}
                    style={{ padding: "5px", minWidth: "200px" }}
                />
                <button onClick={handleCustomInputSubmit}>Submit Custom</button>
                <button onClick={handleRandomize}>Randomize</button>
                <button onClick={handleShuffleOrder}>Shuffle Order</button>
            </div>
        </div>
    );
};

export default Home;
