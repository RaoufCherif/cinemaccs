import { Flex, Box, Stack, Spinner, Image, Link } from "@chakra-ui/react";

import { useGetRoom } from "../data/room";

export const RoomPage = () => {
  const { isLoading, data: room } = useGetRoom();
  if (isLoading) {
    return <Spinner />;
  }
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
