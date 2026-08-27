import type React from "react";

interface IButton {
    id: string;
    name: string;
    value: string;
    label: string;
    onClick?: () => void;
    children?: React.ReactNode;

}

const Button: React.FC<IButton> = (props: IButton) => {
    return (
        <button
            id={props.id}
            name={props.name}
            value={props.value}
            onClick={props.onClick}

        >
            {props.children ? props.children : props.label}
        </button>
    );
}

export default Button;
