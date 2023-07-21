import { useGetMovie } from "../data/movie";
import { Flex, Box, Stack, Image, Link } from "@chakra-ui/react";

import { MovieWithTheaters, Room, Session, Theater } from "./types";
import { useEffect, useState } from "react";
import { ExternalLinkIcon } from "@chakra-ui/icons";

export const RoomPage = () => {
  //   const { data: room } = useGetRoom();
  const room = "toto";
  return (
    <Flex
      flexDirection="column"
      width="100wh"
      height="100vh"
      backgroundColor="gray.200"
      justifyContent="center"
      alignItems="center"
    >
      <Stack
        flexDir="column"
        mb="2"
        justifyContent="center"
        alignItems="center"
      >
        {room ? (
          <>
            {/* TODO utiliser TheaterCard ici */}
            <div>toto</div>
          </>
        ) : (
          <Box>Salle introuvable</Box>
        )}
      </Stack>
    </Flex>
  );
};
