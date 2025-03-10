import React, {useState, useEffect} from "react";
import BarContainer from "../../components/BarContainer/BarContainer";

const Home = () => {
    const [stages, setStages] = useState([]);
    const [currentStep, setCurrentStep] = useState(0);

    useEffect(() => {
        const fetchStages = async () => {
            try {
                const response = await fetch("http://localhost:5000/sort", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({
                        input_data: [23, 56, 12, 87, 34, 78, 45, 91, 3, 67, 14, 98, 29, 71, 8, 42, 55, 19, 63, 80, 37,
                            94, 5, 72, 16, 49, 84, 27, 60, 9, 31, 76, 44, 97, 21, 68, 38, 82, 53, 10, 25, 74, 41, 89, 7,
                            58, 36, 93, 17, 64, 30, 85, 48, 99, 2, 69, 22, 77, 39, 92, 15, 50, 81, 26, 61, 4, 35, 88,
                            20, 73, 46, 96, 11, 54, 83, 32, 70, 18, 57, 90, 6, 40, 75, 28, 62, 13, 47, 95, 24, 79, 33,
                            66, 1, 52, 86, 43, 100, 59, 65, 51],
                        algorithms: "merge",
                    }),
                });
                const result = await response.json();
                setStages(result.stages || []);
                setCurrentStep(0);
            } catch (error) {
                console.error("Error fetching sorting stages:", error);
            }
        };

        fetchStages();
    }, []);

    useEffect(() => {
        if (stages.length === 0) return;

        const interval = setInterval(() => {
            setCurrentStep((prevStep) => {
                if (prevStep >= stages.length - 1) {
                    clearInterval(interval);
                    return prevStep;
                }
                return prevStep + 1;
            });
        }, 100);

        return () => clearInterval(interval);
    }, [stages]);

    return (
        <div style={{display: "flex", justifyContent: "center", alignItems: "center", height: "100vh"}}>
            <BarContainer data={stages[currentStep] || []} height="75%" width="75%"/>
        </div>
    );
};

export default Home;
