import * as React from "react";
import {
  Flex,
  Heading,
  Input,
  Button,
  InputGroup,
  Stack,
  InputLeftElement,
  Box,
  Link,
  Avatar,
  FormControl,
} from "@chakra-ui/react";
const theaters = [
  {
    id: "1",
    name: "MK2 Bibliothèque",
    address: "2 rue de la bibliothèque, 75014 Paris",
  },
  {
    id: "2",
    name: "MK2 Bastille",
    address: "2 rue de la Bastille, 75014 Paris",
  },
  {
    id: "3",
    name: "MK2 Beaubourg",
    address: "2 rue de Beaubourg, 75014 Paris",
  },
];

export const Home = () => (
  <Flex
    flexDirection="column"
    width="100wh"
    height="100vh"
    backgroundColor="gray.200"
    justifyContent="center"
    alignItems="center"
  >
    <Stack flexDir="column" mb="2" justifyContent="center" alignItems="center">
      <Avatar bg="teal.500" />
      <Heading color="teal.400">Bienvenue</Heading>
      <Box minW={{ base: "90%", md: "468px" }}>
        <form>
          <Stack
            spacing={4}
            p="1rem"
            backgroundColor="whiteAlpha.900"
            boxShadow="md"
          >
            <FormControl>
              <InputGroup>
                <InputLeftElement
                  pointerEvents="none"
                  //   children={<CFaUserAlt color="gray.300" />}
                />
                <Input type="text" placeholder="Le chat poté" />
              </InputGroup>
            </FormControl>
            <Button
              borderRadius={0}
              type="submit"
              variant="solid"
              colorScheme="teal"
              width="full"
            >
              Rechercher un film
            </Button>
          </Stack>
        </form>
      </Box>
      <Box minW={{ base: "90%", md: "468px" }}>
        <Stack
          spacing={4}
          p="1rem"
          backgroundColor="whiteAlpha.900"
          boxShadow="md"
        >
          {theaters.map((theater) => (
            <Link href={`/cinema/${theater.id}`}>
              {theater.name}, {theater.address}
            </Link>
          ))}
        </Stack>
      </Box>
    </Stack>
  </Flex>
);

export default Home;
