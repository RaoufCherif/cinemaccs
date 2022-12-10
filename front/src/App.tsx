import * as React from "react";
import {
  ChakraProvider,
  Box,
  Text,
  Link,
  VStack,
  Code,
  Grid,
  theme,
} from "@chakra-ui/react";
import { ColorModeSwitcher } from "./ColorModeSwitcher";
import { Logo } from "./Logo";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import routes from "./routes";
import { Home } from "./Pages/Home";
import { Movie } from "./Pages/Movie";
import { Theater } from "./Pages/Theater";

export const App = () => (
  <ChakraProvider theme={theme}>
    <BrowserRouter>
      <Routes>
        <Route path={routes.home} element={<Home />} />
        <Route path={routes.theater} element={<Theater />} />
        <Route path={routes.movie} element={<Movie />} />
      </Routes>
    </BrowserRouter>
  </ChakraProvider>
);
