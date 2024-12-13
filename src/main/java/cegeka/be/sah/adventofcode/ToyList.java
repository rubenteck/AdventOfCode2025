package cegeka.be.sah.adventofcode;

import java.util.List;

public record ToyList(List<Toy> toys) {
    public getSortedListByType() {
        toys.stream()
                .reduce(0, (subtotal, toy) -> subtotal +toy.getAmount())
                .groupingBy(Toy::type);
    }
}
