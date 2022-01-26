import datetime
import time



order_no01=['XgPLJGizXcTe', 'XgPLJFtDbYhi', 'XgPLJGfxLsyE', 'XgPLJGqrvSPX', 'XgPLJGc6j93Y', 'XgPLJFxwu6Ji', 'XgPLJFiiWrYs', 'XgPLJFuKEhZq', 'XgPLJGjkMqgF', 'XgPLJGgvj4NY', 'XgPLK5fjnue6', 'XgPLJZfE6Gh8', 'XgPLK5gGRB4v', 'XgPLJZkkCkuq', 'XgPLJZtS84HV', 'XgPLK7kZLBNR', 'XgPLK2BFpFiX', 'XgPLK4fxRrBX', 'XgPLK7tW3Apw', 'XgPLK85W6RzP', 'XgPLKkHVGERN', 'XgPLKpBBEcDs', 'XgPLKpF8GdcC', 'XgPLKpLDpLiF', 'XgPLKqtw8c7T', 'XgPLKrx5D93Q', 'XgPLKsz9QxR6', 'XgPLKsVNrFj2', 'XgPLKuiqW9xs', 'XgPLKsuaUiqv', 'XgPLKA8qhw8Y', 'XgPLKMzvyFF4', 'XgPLKMHyjrn5', 'XgPLKNBgsTcy', 'XgPLKNMcUsJM', 'XgPLKQwxfp8Y', 'XgPLKRUEKc92', 'XgPLKTpJEn4k', 'XgPLKTrmDbMh', 'XgPLKV5MzVq8', 'XgPLKVPj9qTW', 'XgPLKYeXtWcU', 'XgPLKYgZUZcm', 'XgPLL49yifk7', 'XgPLL5GD9W3V', 'XgPLL7Fdn7cy', 'XgPLL8YfEnF2', 'XgPLL8Z63GWu', 'XgPLLa5C2CPT', 'XgPLLchqirrV', 'XgPLLc5xTmYe', 'XgPLLdt4VnNZ', 'XgPLLdskqMLL', 'XgPLLgJpv5D9', 'XgPLLiQtrCJJ', 'XgPLLjDQQPaM', 'XgPLLpkrvBwv', 'XgPLLq5G7gLZ', 'XgPLLquavawT', 'XgPLLsQjEtgy', 'XgPLLtw3UuwL', 'XgPLLu6dBCUD', 'XgPLLv2mH4kr', 'XgPLLws9wWVU', 'XgPLLyRdg7iN', 'XgPLLyAaFuFX', 'XgPLLASxHB4t', 'XgPLLDX3Mpf9', 'XgPLLEeiRNCN', 'XgPLLG96sVhx', 'XgPLLGrJzetB', 'XgPLLGzsMGdE', 'XgPLLHiW4e5u', 'XgPLLJi4NxBM', 'XgPLLKZNj3jg', 'XgPLLLNVmqTb', 'XgPLLMq7sftK', 'XgPLLReg9wTh', 'XgPLLTRuNWKH', 'XgPLLTWCCVse', 'XgPLLU6s9FFW', 'XgPLLUuireZK', 'XgPLLWGrxCMW', 'XgPLLWF4wNBS', 'XgPLLYbteZtL', 'XgPLLYYHrspz', 'XgPLLYPGrsPH', 'XgPLM4uXFQC4', 'XgPLM4YFtq7F', 'XgPLM7D6N3H3', 'XgPLM9RTnHS6', 'XgPLM9p9PDcG', 'XgPLMa6LAHVZ', 'XgPLMaXxQDHp', 'XgPLMbWuTUWN', 'XgPLMcwDpMS5', 'XgPLMdsXvwCg', 'XgPLMenkeTnW', 'XgPLMgfmSdUR', 'XgPLMiQ7ew2j', 'XgPLMm45KV8X', 'XgPLMmSJkgRt', 'XgPLMn7BembG', 'XgPLMncnS8AP', 'XgPLMqKhnbt5', 'XgPLMqKrMNk7', 'XgPLMr2renYz', 'XgPLMrMdBnzx', 'XgPLMsPTwPPY', 'XgPLMxpw6Myy', 'XgPLMDpenMnS', 'XgPLMFHJy6dw', 'XgPLMGgRpZTx', 'XgPLMGxMVEAT', 'XgPLMH5dhdsq', 'XgPLMHUsNHjX', 'XgPLMHUmyvZe', 'XgPLMKw4QUg5', 'XgPLMLnFNUdU', 'XgPLMNreTbtk', 'XgPLMR23xPRV', 'XgPLMU8jke4W', 'XgPLMUy7MmbW', 'XgPLMYWJNPND', 'XgPLMYXbaEzC', 'XgPLMZzNTNuG', 'XgPLMZUx35vw', 'XgPLN24N8ryp', 'XgPLMZLwyRfs', 'XgPLN288q4Fk', 'XgPLN5HTVdRi', 'XgPLN7xMjm6x', 'XgPLN9zCvhJ4', 'XgPLNdDg3WgY', 'XgPLNeNYqiQt', 'XgPLNf7iKuan', 'XgPLNg4MK3Gu', 'XgPLNgsJtu4V', 'XgPLNgG7UyFM', 'XgPLNhcSMgDf', 'XgPLNiYapnme', 'XgPLNmjdbXDt', 'XgPLNn9FrdM4', 'XgPLNqCWJDTQ', 'XgPLNrWmQjZV', 'XgPLNuLVn6n2', 'XgPLNuNemALV', 'XgPLNwxNdEVh', 'XgPLNwwX2nBm', 'XgPLNwFiNDpT', 'XgPLNx6Yjw8Y', 'XgPLNxXuznnF', 'XgPLNzFBhVGF', 'XgPLNBBGy2m9', 'XgPLNDRQAZBR', 'XgPLNEiwquCJ', 'XgPLNGmfkkfh', 'XgPLNJfVUSi9', 'XgPLNLc5Lf8x', 'XgPLNM8ptWXW', 'XgPLNM6ggTTi', 'XgPLNN5JR36T', 'XgPLNP5cdbYj', 'XgPLNS4nfLiE', 'XgPLNSZhekyE', 'XgPLNSYQ9TvG', 'XgPLNVqM3STm', 'XgPLNVwJz4iH', 'XgPLNYQfNF3B', 'XgPLNZkQuQNR', 'XgPLP22uc5Er', 'XgPLP2qxUGWc', 'XgPLP3WWXFMV', 'XgPLP6HiP5fP', 'XgPLP85yv4Xu', 'XgPLP8YYH3ie', 'XgPLP9E4yDbn', 'XgPLPa39sfeK', 'XgPLPdSQ2u3U', 'XgPLPetGNzSP', 'XgPLPeCZGhZp', 'XgPLPfzPjEDc', 'XgPLPfFUGXXN', 'XgPLPisAUwAG', 'XgPLPkG5jPzx', 'XgPLPmxALXvA', 'XgPLPn7FwNJK', 'XgPLPnuXiScm', 'XgPLPsA9Pzc2', 'XgPLPsVkSiBh', 'XgPLPu8nBJfd', 'XgPLPuML5UpQ', 'XgPLPx3rJHSp', 'XgPLPycHEqUy', 'XgPLPDzV64gt', 'XgPLPEmrct24', 'XgPLPDajCvYr', 'XgPLPCNUjM9B', 'XgPLPCXzyAYs', 'XgPLPFwXUcWu']
order_no02=['XgPLK7tW3Apw', 'XgPLLU6s9FFW', 'XgPLJFiiWrYs', 'XgPLJZkkCkuq', 'XgPLLYYHrspz', 'XgPLJFuKEhZq', 'XgPLLWF4wNBS', 'XgPLLsQjEtgy', 'XgPLLReg9wTh', 'XgPLJGfxLsyE', 'XgPLLLNVmqTb', 'XgPLLG96sVhx', 'XgPLLWGrxCMW', 'XgPLJGgvj4NY', 'XgPLLASxHB4t', 'XgPLJZfE6Gh8', 'XgPLLEeiRNCN', 'XgPLK2BFpFiX', 'XgPLM4YFtq7F', 'XgPLJFtDbYhi', 'XgPLLyRdg7iN', 'XgPLJZtS84HV', 'XgPLKsVNrFj2', 'XgPLLYPGrsPH', 'XgPLKsuaUiqv', 'XgPLKrx5D93Q', 'XgPLL49yifk7', 'XgPLLu6dBCUD', 'XgPLLa5C2CPT', 'XgPLKpF8GdcC', 'XgPLKsz9QxR6', 'XgPLL8Z63GWu', 'XgPLKkHVGERN', 'XgPLLpkrvBwv', 'XgPLKuiqW9xs', 'XgPLKMzvyFF4', 'XgPLLchqirrV', 'XgPLL8YfEnF2', 'XgPLL5GD9W3V', 'XgPLK5gGRB4v', 'XgPLLq5G7gLZ', 'XgPLKV5MzVq8', 'XgPLLc5xTmYe', 'XgPLLquavawT', 'XgPLKYgZUZcm', 'XgPLKMHyjrn5', 'XgPLKNMcUsJM', 'XgPLKA8qhw8Y', 'XgPLLws9wWVU', 'XgPLKQwxfp8Y', 'XgPLK4fxRrBX', 'XgPLKTpJEn4k', 'XgPLKpLDpLiF', 'XgPLJGjkMqgF', 'XgPLJFxwu6Ji', 'XgPLLTWCCVse', 'XgPLLyAaFuFX', 'XgPLLv2mH4kr', 'XgPLLGrJzetB', 'XgPLLGzsMGdE', 'XgPLLTRuNWKH', 'XgPLJGizXcTe', 'XgPLMmSJkgRt', 'XgPLK85W6RzP', 'XgPLMiQ7ew2j', 'XgPLMGxMVEAT', 'XgPLNM6ggTTi', 'XgPLLiQtrCJJ', 'XgPLMncnS8AP', 'XgPLP8YYH3ie', 'XgPLMcwDpMS5', 'XgPLPnuXiScm', 'XgPLMenkeTnW', 'XgPLPfFUGXXN', 'XgPLJGc6j93Y', 'XgPLLYbteZtL', 'XgPLKVPj9qTW', 'XgPLNJfVUSi9', 'XgPLMn7BembG', 'XgPLMYWJNPND', 'XgPLMxpw6Myy', 'XgPLP22uc5Er', 'XgPLM9RTnHS6', 'XgPLLdt4VnNZ', 'XgPLPisAUwAG', 'XgPLNYQfNF3B', 'XgPLMDpenMnS', 'XgPLMgfmSdUR', 'XgPLMdsXvwCg', 'XgPLN5HTVdRi', 'XgPLLdskqMLL', 'XgPLMHUsNHjX', 'XgPLL7Fdn7cy', 'XgPLNqCWJDTQ', 'XgPLM9p9PDcG', 'XgPLMZUx35vw', 'XgPLK7kZLBNR', 'XgPLNwxNdEVh', 'XgPLNuNemALV', 'XgPLPmxALXvA', 'XgPLMFHJy6dw', 'XgPLKqtw8c7T', 'XgPLNGmfkkfh', 'XgPLNhcSMgDf', 'XgPLLJi4NxBM', 'XgPLMGgRpZTx', 'XgPLPa39sfeK', 'XgPLN24N8ryp', 'XgPLMr2renYz', 'XgPLNN5JR36T', 'XgPLMm45KV8X', 'XgPLLUuireZK', 'XgPLJGqrvSPX', 'XgPLMaXxQDHp', 'XgPLLjDQQPaM', 'XgPLKYeXtWcU', 'XgPLLMq7sftK', 'XgPLMUy7MmbW', 'XgPLNwFiNDpT', 'XgPLKpBBEcDs', 'XgPLLKZNj3jg', 'XgPLM4uXFQC4', 'XgPLK5fjnue6', 'XgPLPsA9Pzc2', 'XgPLNS4nfLiE', 'XgPLM7D6N3H3', 'XgPLKNBgsTcy', 'XgPLPdSQ2u3U', 'XgPLN9zCvhJ4', 'XgPLLtw3UuwL', 'XgPLP2qxUGWc', 'XgPLLgJpv5D9', 'XgPLNf7iKuan', 'XgPLNuLVn6n2', 'XgPLNgG7UyFM', 'XgPLKRUEKc92', 'XgPLNVqM3STm', 'XgPLMqKhnbt5', 'XgPLNSYQ9TvG', 'XgPLMH5dhdsq', 'XgPLNLc5Lf8x', 'XgPLMNreTbtk', 'XgPLNwwX2nBm', 'XgPLNP5cdbYj', 'XgPLLHiW4e5u', 'XgPLMU8jke4W', 'XgPLMa6LAHVZ', 'XgPLNxXuznnF', 'XgPLNSZhekyE', 'XgPLNmjdbXDt', 'XgPLLDX3Mpf9', 'XgPLN7xMjm6x', 'XgPLN288q4Fk', 'XgPLNiYapnme', 'XgPLNVwJz4iH', 'XgPLPeCZGhZp', 'XgPLMZLwyRfs', 'XgPLMZzNTNuG', 'XgPLMrMdBnzx', 'XgPLNDRQAZBR', 'XgPLPkG5jPzx', 'XgPLMLnFNUdU', 'XgPLPDajCvYr', 'XgPLMsPTwPPY', 'XgPLNn9FrdM4', 'XgPLNzFBhVGF', 'XgPLPsVkSiBh', 'XgPLP9E4yDbn', 'XgPLMHUmyvZe', 'XgPLPCNUjM9B', 'XgPLNrWmQjZV', 'XgPLMqKrMNk7', 'XgPLP85yv4Xu', 'XgPLP3WWXFMV', 'XgPLNBBGy2m9', 'XgPLNx6Yjw8Y', 'XgPLPx3rJHSp', 'XgPLNZkQuQNR', 'XgPLPu8nBJfd', 'XgPLPn7FwNJK', 'XgPLPfzPjEDc', 'XgPLP6HiP5fP', 'XgPLMbWuTUWN', 'XgPLPDzV64gt', 'XgPLNEiwquCJ', 'XgPLNeNYqiQt', 'XgPLPEmrct24', 'XgPLPycHEqUy', 'XgPLPFwXUcWu', 'XgPLMR23xPRV', 'XgPLMYXbaEzC', 'XgPLPuML5UpQ', 'XgPLNM8ptWXW', 'XgPLNdDg3WgY', 'XgPLPCXzyAYs']
order_no02=['Xh2LnUnuZM9m', 'Xh2LnTBs9A39', 'Xh2LnTmk5ncw', 'Xh2LnTd5Ubam', 'Xh2LnT8hwcrd', 'Xh2LnTyvx3Mq', 'Xh2LnT9tQud5', 'Xh2LnTNKafr7', 'Xh2LnUQmy4xY', 'Xh2LnU7Tbhpj', 'Xh2Lphhvn73Z', 'Xh2LpkZLRDCH', 'Xh2LpmKygmtV', 'Xh2Lpm2dmDKN', 'Xh2LpmNBJYb9', 'Xh2Lpm8exGdJ', 'Xh2LpmFtsdE7', 'Xh2LpmvPS5ft', 'Xh2Lpn7GZgXp', 'Xh2LpmeSSHW3', 'Xh2LpKqxABpY', 'Xh2LpJS69uDr', 'Xh2LpK6KUp2p', 'Xh2LpJySPMZV', 'Xh2LpJxJVzpP', 'Xh2LpJATBqes', 'Xh2LpGW3tDd2', 'Xh2LpDuc5Xk8', 'Xh2LpKP8XEcp', 'Xh2LpK4aDLJE', 'Xh2Lqh5gZxPc', 'Xh2LqigQt97i', 'Xh2Lqj2CdBax', 'Xh2Lqih9FFhv', 'Xh2LqkCQYVVP', 'Xh2LqhVzWJmd', 'Xh2Lqi4f2ehV', 'Xh2Lqkwk8jGc', 'Xh2LqjqyzW6Z', 'Xh2LqjNJ6dRh', 'Xh2LqLciBZBE', 'Xh2LqJgiqr6x', 'Xh2LqJEZmScX', 'Xh2LqMFRQuGr', 'Xh2LqMJ3EeN6', 'Xh2LqLPufrQq', 'Xh2LqG4m5FCL', 'Xh2LqMs4pHNa', 'Xh2LqMGZ7LyK', 'Xh2LqNVqqqRi', 'Xh2LrcWfMMeq', 'Xh2Lrd8G7HXM', 'Xh2Lrd8BRFg4', 'Xh2LrgBDQwzi', 'Xh2LrekitjSv', 'Xh2LrfyZvD9n', 'Xh2LrgwSiQa8', 'Xh2LrgwJ85rm', 'Xh2LreC3pfTC', 'Xh2Lri8JVJuR', 'Xh2LrE6Qja6Y', 'Xh2LrC6Zuifx', 'Xh2LrCqEez3n', 'Xh2LrG4jbnPp', 'Xh2LrFfqYDxX', 'Xh2LrGFS3Wna', 'Xh2LrELzxuqG', 'Xh2LrHMaHCU6', 'Xh2LrGq4PjPS', 'Xh2LrG76cTJ6', 'Xh2Ls9nLWAPe', 'Xh2Lsb3ZNLhm', 'Xh2Lsbm3y4iV', 'Xh2LscwfiNaQ', 'Xh2LsbQxTw6a', 'Xh2LscGsxLfy', 'Xh2Lsb9z5i23', 'Xh2LsextBVmp', 'Xh2LseuHTtju', 'Xh2LseDUgUP5', 'Xh2LsBvDcbhk', 'Xh2LsyaRZndP', 'Xh2LsDkhyeAq', 'Xh2LsBqCMQjm', 'Xh2LsDxhzydW', 'Xh2LsDkPtamD', 'Xh2LsEWVatKK', 'Xh2LsDxnW76p', 'Xh2LsDVfqvf4', 'Xh2LsF4zBDni', 'Xh2LtaaukNK8', 'Xh2Lt9dBfz2K', 'Xh2Lt9Lk6r8Z', 'Xh2Ltaxuz4sq', 'Xh2LtakFJz5A', 'Xh2LtaB7bLnB', 'Xh2Lt8QT3vDX', 'Xh2Lt8etVDhg', 'Xh2Lt82YA5cQ', 'Xh2LtbWYQYQs', 'Xh2LtRMALCrv', 'Xh2LtNeerHnj', 'Xh2LtM5LivwV', 'Xh2LtL9YYkci', 'Xh2LtQTfyfcp', 'Xh2LtTFB663y', 'Xh2LtRtiY4gz', 'Xh2LtNvdGaYk', 'Xh2LtUP7uGmw', 'Xh2LtWNxrkX7', 'Xh2LuvffgVUp', 'Xh2LupNZEHfj', 'Xh2LuuuJK6jz', 'Xh2LussJqP9v', 'Xh2Lurgriv4S', 'Xh2Lutx8Rmra', 'Xh2Luwhf9KVr', 'Xh2Lus48bSrH', 'Xh2LuqCwjfMD', 'Xh2Luu2UQWKT', 'Xh2LvzACd5fA', 'Xh2LvyKgB8ad', 'Xh2LvzJQBiMd', 'Xh2LvzAXSmFk', 'Xh2LvExCfkev', 'Xh2LvB5JGAsz', 'Xh2LvyKuwtDV', 'Xh2LvATtkUMh', 'Xh2LvB5fPzwH', 'Xh2LvAyiXjku', 'Xh2LwqNqsVjn', 'Xh2Lwt4iG5kL', 'Xh2LwtJncKty', 'Xh2LwtPQBMGr', 'Xh2LwrHXnMKk', 'Xh2Lwu2nN8JN', 'Xh2LwtjkED4z', 'Xh2LwuM78qHB', 'Xh2LwvJ48e8F', 'Xh2Lwz4bGBKP', 'Xh2LwWNyM3hX', 'Xh2Lx6kQsgYD', 'Xh2Lx6FA5vji', 'Xh2Lx6HmeEAH', 'Xh2Lx8zHC7Sj', 'Xh2Lx8aZTvw9', 'Xh2Lx7viwwuq', 'Xh2Lx8T6zWbi', 'Xh2Lxb6bJabD', 'Xh2LxdccYRVX', 'Xh2LxtyJiLPm', 'Xh2Lxvbz9fEf', 'Xh2LxsueVsEz', 'Xh2LxzFzw4Xq', 'Xh2LxCWsqjyc', 'Xh2LxAyE75xp', 'Xh2LxAfskFjX', 'Xh2LxDD7cTiM', 'Xh2LxDr3i8Re', 'Xh2LxK98RGrh', 'Xh2LxSRA4FrL', 'Xh2LxXm4ArFQ', 'Xh2LxUtFRvLj', 'Xh2LxUBfxDGC', 'Xh2LybrGMgct', 'Xh2LyaMvRaR8', 'Xh2Ly9VVJsgZ', 'Xh2LycUtNv49', 'Xh2LybcUK5ej', 'Xh2LygjuGdyB', 'Xh2LyqDEw76F', 'Xh2LywdJ5hGE', 'Xh2LyxquzqNY', 'Xh2LyATWmuN6', 'Xh2LyG3ZgJWY', 'Xh2LyKgZRbpP', 'Xh2LyPhv36Gb', 'Xh2LyLKYb4tx', 'Xh2LyLcRe4aS', 'Xh2LyScJXNKZ', 'Xh2LyVBMZHvs', 'Xh2LyZwipqbE', 'Xh2LzaCAtXZc', 'Xh2Lz8Hx84mG', 'Xh2Lz7ZDfaQy', 'Xh2LzcrwiAaN', 'Xh2Lzf9JxC4E', 'Xh2Lzgzcky3g', 'Xh2LzigkQB3y', 'Xh2Lzssn7VSL', 'Xh2LzygcxjE5', 'Xh2LzufR7Hr3', 'Xh2Lzwe2GqKN', 'Xh2LzCGGRkKW', 'Xh2LzGvT8ayD', 'Xh2LzGtag9CK', 'Xh2LzGttGR9x', 'Xh2LzVbE2rUS', 'Xh2LzNbZZxba', 'Xh2LzYH9m8L4', 'Xh2LzKZcuYu2', 'Xh2LA265ZDe9', 'Xh2LA42vbFBV', 'Xh2LA9wSfuUQ', 'Xh2LAhksURyZ', 'Xh2LA9hcYUgv', 'Xh2LAuKVikVQ', 'Xh2LAuX4GEDR', 'Xh2LAA3DSYTU', 'Xh2LAAwtixdt', 'Xh2LABWzqSVm', 'Xh2LABYBHnt2', 'Xh2LARawMmSB', 'Xh2LAJdBpHmB', 'Xh2LAMw7KhdR', 'Xh2LAXf9BaxL', 'Xh2LB2h59yWb', 'Xh2LB42UUzKR', 'Xh2LB5tVYYfh', 'Xh2LB6mvq8wt', 'Xh2LBf9Csp77', 'Xh2LBqWMMXJU', 'Xh2LBqEp3wnr', 'Xh2LBtaREqZj', 'Xh2LBwxiHDeW', 'Xh2LBxv3Q5Ay', 'Xh2LBDs6eMn8', 'Xh2LBGGFHdzV', 'Xh2LBLGDcxYU', 'Xh2LBRiCcScX', 'Xh2LBVzE9FRn', 'Xh2LBYpvQPNC', 'Xh2LC4h6tKiK', 'Xh2LC2H2uExQ', 'Xh2LC6Y8u5Q6', 'Xh2LCaY5Rk48', 'Xh2LCr4EqDxh', 'Xh2LCrRQ9YHz', 'Xh2LCN8JmRGG', 'Xh2LCNBa2f7z', 'Xh2LCHvSmWnq', 'Xh2LCTPj72gC', 'Xh2LCPT8nqfX', 'Xh2LCD7w49q6', 'Xh2LCD7m6TEL', 'Xh2LCWfMBr5f', 'Xh2LCZPv23FP', 'Xh2LCZZHakFF', 'Xh2LDhcTmjGa', 'Xh2LDmzSxgRb', 'Xh2LDnNrw9BU', 'Xh2LDpu6fDMR', 'Xh2LDj9wwAha', 'Xh2LDtXxc3SF', 'Xh2LDwUQ4sgw', 'Xh2LDwXdA34e', 'Xh2LDy6WrfF6', 'Xh2LDv2xB9cc', 'Xh2LE2YzXZjb', 'Xh2LDZFrpgaj', 'Xh2LE3qtp5D6', 'Xh2LE2v47nV2', 'Xh2LE4tjBNi8', 'Xh2LE44P2kcQ', 'Xh2LE63HuTqF', 'Xh2LE7EybHbE', 'Xh2LE8C6qrbD', 'Xh2LEaSfWP5G', 'Xh2LEGRXabdb', 'Xh2LEGMnnw8b', 'Xh2LEJD3yLca', 'Xh2LEJMByKea', 'Xh2LEJL23TbJ', 'Xh2LEMF327yE', 'Xh2LEPqstryJ', 'Xh2LEUHxmuL3', 'Xh2LEVZBdKz2', 'Xh2LF4B7nGwN', 'Xh2LFqmB9gWY', 'Xh2LFpdCsCen', 'Xh2LFsuA4Gdu', 'Xh2LFvun4feK', 'Xh2LFw9m9b9e', 'Xh2LFxgiVJ5z', 'Xh2LFD2xjJEf', 'Xh2LFCizDjg8', 'Xh2LFDgQAtQm', 'Xh2LFJ6PjbPV', 'Xh2LFVgBJPWr', 'Xh2LFVJXER7n', 'Xh2LG6fDSmpD', 'Xh2LG2QN5wuP', 'Xh2LG8KaWuyn', 'Xh2LG7R7RRem', 'Xh2LGjyvxt4j', 'Xh2LGfKQ9Qgu', 'Xh2LGpdYTQWW', 'Xh2LGicgVi4F', 'Xh2LGvYRiCve', 'Xh2LGwTmzRZC', 'Xh2LGFaXNXHx']
#Xh2Ka3W4QPMC
#Xh2Tn6F7UDQC


list=[]
list01=[]
#写入text
path = "C:\\test\\michid.txt"
f = open(path, mode="r")
lines=f.readlines()
for lines in lines:
    list.append(lines.strip('\n'))
    for k in range(0,len(list)):
        if  list[k] in list01:
            pass
        else:
            list01.append(list[k])
print(len(list))
print(len(list01))
print(list01)


# for i in range(0,len(order_no02)):
#     if order_no02[i] in order_no01:
#         order_no01.remove(order_no02[i])
#     else:
#         pass
# print(len(order_no01))
# print(order_no01)
# ['XgPLKTrmDbMh', 'XgPLMKw4QUg5', 'XgPLNg4MK3Gu', 'XgPLNgsJtu4V', 'XgPLPetGNzSP']









# print 'tasks done, now sleeping for 10 seconds'















# list=['XfL2iMdzsph8', 'XfL2j2Ydpbwe', 'XfL2jgUUqwdX', 'XfL2jvN4GaeV', 'XfL2jKeJPJjD', 'XfL2jWW4g645', 'XfL2keq5S3B9', 'XfL2ks57jXAQ', 'XfL2kF9c7zQd', 'XfL2mCpAFQjE', 'XfL2mRsS6tWp', 'XfL2n6x9Mewd', 'XfL2nhZi6J5F', 'XfL2nxtUhLxV', 'XfL2nKrYQmr7', 'XfL2nVB26kAz', 'XfL2p8YMWThh', 'XfL2pidqLuZ8', 'XfL2pvRaSGpZ', 'XfL2pHJbakrY', 'XfL2pUJSnP2i', 'XfL2qaJbZM8Z', 'XfL2qkhdkGWB', 'XfL2qybJeSYL', 'XfL2qL48Y99D', 'XfL2qWqKbeqh', 'XfL2r7rjY5m7', 'XfL2rfAiNatf', 'XfL2rsmacZ5c', 'XfL2rCTXVB8H', 'XfL2rN7KjPzS', 'XfL2sMVs2BhQ', 'XfL2tkujJXcM', 'XfL2tCkG42Ge', 'XfL2tSitdfBi', 'XfL2u3MATvjS', 'XfL2ucMntxUv', 'XfL2umfnyBug', 'XfL2uwDrmgnr', 'XfL2uEYSZs37', 'XfL2uX86cw7Q', 'XfL2v7MxrjBG', 'XfL2vq9dZubz', 'XfL2vBJBnMYz', 'XfL2vNryBAjz', 'XfL2w22Wm8pV', 'XfL2wjap4UAz', 'XfL2wwijcP2J', 'XfL2wLvtVjSq', 'XfL2wVjPGNGc', 'XfL2x7ySJjaK', 'XfL2xjkvWFbY', 'XfL2xuk4wvaq', 'XfL2xGSUwPmj', 'XfL2xXiuw2k7', 'XfL2ybTvQxvu', 'XfL2yqaPjGrD', 'XfL2yBZyfn4a', 'XfL2yP9tb7Q7', 'XfL2yYqTPNKc', 'XfL2z99GA6Bf', 'XfL2zhSAjcUM', 'XfL2zt4evFkD', 'XfL2zDFNcjwY', 'XfL2zNvYjyn6', 'XfL2A2aMQGKq', 'XfL2Ad3HHiQC', 'XfL2AqxSurL7', 'XfL2ABKzemCT', 'XfL2AQMKhNga', 'XfL2B4QqZLpG', 'XfL2BgCRWCvD', 'XfL2Bup7rpzi', 'XfL2BJatHLgF', 'XfL2BVYn7mGY', 'XfL2C8TazyPr', 'XfL2CjJbY88d', 'XfL2CxhnNxHL', 'XfL2CKbiVNSg', 'XfL2CVDDJVk3', 'XfL2D7tAU6wM', 'XfL2Dj5LbtCP', 'XfL2DwpRhchK', 'XfL2DGvhfBE3', 'XfL2DSpZaJgU', 'XfL2E53qTkML', 'XfL2EgT9sWkL', 'XfL2EuJ5t66Z', 'XfL2EFncpqRc', 'XfL2ESztAzxL', 'XfL2F4yK37YG', 'XfL2FefEfSej', 'XfL2FpneCV9r', 'XfL2FxsM7eVa', 'XfL2FFW5a2dE', 'XfL2FQRfgxX5', 'XfL2FZnmFqfs', 'XfL2G9KzGiLn', 'XfL2GhddR2Zu', 'XfL2GrmB6NrU']
# lsit01=['XfL2iMdzsph8', 'XfL2j2Ydpbwe', 'XfL2jgUUqwdX', 'XfL2jvN4GaeV', 'XfL2jKeJPJjD', 'XfL2jWW4g645', 'XfL2keq5S3B9', 'XfL2ks57jXAQ', 'XfL2kF9c7zQd', 'XfL2mCpAFQjE', 'XfL2mRsS6tWp', 'XfL2n6x9Mewd', 'XfL2nhZi6J5F', 'XfL2nxtUhLxV', 'XfL2nKrYQmr7', 'XfL2nVB26kAz', 'XfL2p8YMWThh', 'XfL2pidqLuZ8', 'XfL2pvRaSGpZ', 'XfL2pHJbakrY', 'XfL2pUJSnP2i', 'XfL2qaJbZM8Z', 'XfL2qkhdkGWB', 'XfL2qybJeSYL', 'XfL2qL48Y99D', 'XfL2qWqKbeqh', 'XfL2r7rjY5m7', 'XfL2rfAiNatf', 'XfL2rsmacZ5c']
#
# for i in range(0,len(lsit01)):
#     if lsit01[i] in list:
#         list.remove(lsit01[i])
#     else:
#         pass
# print(len(list))
# print(list)





list=["1","2","3","4","5","6",]




from concurrent.futures import ThreadPoolExecutor
import time

# def spider(page):
#     time.sleep(page)
#     print(f"crawl task{page} finished")
#     return page
#
# with ThreadPoolExecutor(max_workers=5) as t:  # 创建一个最大容纳数量为5的线程池
#         task1 = t.submit(spider, 1)
#         task2 = t.submit(spider, 2)  # 通过submit提交执行的函数到线程池中
#         task3 = t.submit(spider, 3)
#
#         print(f"task1: {task1.done()}")  # 通过done来判断线程是否完成
#         print(f"task2: {task2.done()}")
#         print(f"task3: {task3.done()}")
#
#         time.sleep(5)
#         print(f"task1: {task1.done()}")
#         print(f"task2: {task2.done()}")
#         print(f"task3: {task3.done()}")
#         print(task1.result())  # 通过result来获取返回值

