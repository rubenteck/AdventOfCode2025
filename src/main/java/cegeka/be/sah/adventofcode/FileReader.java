package cegeka.be.sah.adventofcode;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;

import java.io.IOException;

public record FileReader(@Value("classpath:data/data.json") Resource resourceFile) {
    private static final ObjectMapper objectMapper = new ObjectMapper();

    public ToyList readToyList() throws IOException {
        return objectMapper.readValue(resourceFile.getFile(), ToyList.class);
    }
}
