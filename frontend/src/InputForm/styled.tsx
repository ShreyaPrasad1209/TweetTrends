import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center;
  justify-content: center;
  height: fit-content;
  width: fit-content;
  margin: auto;
`;

export const Input = styled.input`
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 300px;
  display: flex;
  &:hover {
    border-color: #0056b3;
  }
  &:focus {
    box-shadow: 0 0 8px rgba(0, 123, 255, 0.6), 0 4px 8px rgba(0, 0, 0, 0.25);
    border-color: #0056b3;
  }
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  transition: border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
`;

export const Select = styled.select`
  padding: 10px;
  border-radius: 5px;
  width: 320px;
  &:hover {
    border-color: #0056b3;
  }
  &:focus {
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
  }
  transition: border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
`;

export const Logo = styled.img`
  width: 97px;
  height: 86px;
  margin-top: 1.3rem;
  @media (max-width: 768px) {
    width: 80px;
    height: 80px;
  }
`;

export const Title = styled.h2`
  width: 14rem;
  font-family: "Lato", sans-serif;
  font-weight: 600;
  font-style: normal;
`;

export const TitleLogoWrapper = styled.div`
  display: flex;
`;

export const Button = styled.button`
  padding: 10px 20px;
  background-color: #1da1f2;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;

  &:hover {
    background-color: #134e6c;
  }
`;

export const UserProfileContainer = styled.div`
  display: flex;
  flex-direction: column;
  flex-flow: row wrap;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  padding: 20px;
`;
