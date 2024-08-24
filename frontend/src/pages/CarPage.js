import React from 'react';
import {CarForm} from "../components/CarForm";
import {Chat} from "../components/Chat";
import {Cars} from "../components/Cars";

const CarPage = () => {
    return (
        <div>
            <CarForm/>
            <hr/>
            <Cars/>
            <hr/>
            <Chat/>
        </div>
    );
};


export {CarPage};