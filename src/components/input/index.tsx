import type React from "react";

interface IInput {
    id: string;
    name: string;
    type?: string;
    value?: string;
    placeholder?: string;
    label?: string;
    onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const Input: React.FC<IInput> = ({ 
    id, 
    name, 
    type = "text", 
    value, 
    placeholder, 
    label, 
    onChange 
}: IInput) => {
    return (
        <div style={{ display: "flex", flexDirection: "column", gap: "4px", marginBottom: "12px", textAlign: "left" }}>
            {label && <label htmlFor={id} style={{ fontWeight: "bold" }}>{label}</label>}
            <input
                id={id}
                name={name}
                type={type}
                value={value}
                placeholder={placeholder}
                onChange={onChange}
                style={{ 
                    padding: "8px", 
                    borderRadius: "4px", 
                    border: "1px solid #ccc",
                    fontSize: "16px"
                }}
            />
        </div>
    );
}

export default Input;
