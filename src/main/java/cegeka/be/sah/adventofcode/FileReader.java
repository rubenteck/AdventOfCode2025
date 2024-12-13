package cegeka.be.sah.adventofcode;

import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;

import java.io.IOException;
import java.util.Objects;

@RequiredArgsConstructor
public final class FileReader {
    private final ObjectMapper objectMapper = new ObjectMapper();
    @Value("classpath:example_input/opdracht1TestInput.json")
    private Resource resourceFile;

    public ToyList readToyList() throws IOException {
        return objectMapper.readValue(resourceFile.getFile(), ToyList.class);
    }
}
