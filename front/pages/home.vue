<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12" md="7">
        <v-card class="fill-height">
          <v-card-title>
            <v-btn rounded text x-large>
              <v-icon left>mdi-truck-outline</v-icon>
              Commandes reçues
            </v-btn>
          </v-card-title>
          <v-card-text>
            <v-simple-table>
              <template v-slot:default>
                <thead>
                  <tr>
                    <th class="text-left text-h6">Nom du client</th>
                    <th class="text-left text-h6">Prix TTC</th>
                    <th class="text-center text-h6">Préparateur</th>
                    <th class="text-center text-h6">Livreur</th>
                    <th class="text-left text-h6"></th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(order, index) in lastOrders" :key="index">
                    <td>{{ order.client }}</td>
                    <td>{{ order.priceTTC }}</td>
                    <td class="text-center">
                      <template v-if="!!order.orderPicker">
                        {{ order.orderPicker }}
                      </template>
                      <template v-else>
                        <v-btn
                          rounded
                          outlined
                          small
                          color="info"
                          style="text-transform: none"
                        >
                          Assigner un préparateur
                        </v-btn>
                      </template>
                    </td>
                    <td class="text-center">
                      <template v-if="!!order.deliveryMan">
                        {{ order.deliveryMan }}
                      </template>
                      <template v-else>
                        <v-btn
                          rounded
                          outlined
                          small
                          color="info"
                          style="text-transform: none"
                        >
                          Assigner un livreur
                        </v-btn>
                      </template>
                    </td>
                    <td>
                      <v-btn rounded outlined small color="success">
                        Confirmer
                      </v-btn>
                    </td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="5">
        <v-row>
          <v-col cols="12" sm="6" class="pt-0">
            <v-card>
              <v-card-title>
                <v-icon left>mdi-crown</v-icon>
                Top client
              </v-card-title>
              <v-card-text>
                <v-card flat outlined>
                  <v-card-text class="py-0">
                    <v-list dense>
                      <v-list-item
                        v-for="(client, index) in topClients"
                        :key="index"
                      >
                        <v-list-item-icon>
                          <v-icon
                            :color="
                              index === 0
                                ? 'primary'
                                : index === 1
                                ? 'success'
                                : 'warning'
                            "
                            >mdi-medal</v-icon
                          >
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>
                            {{ client.name }}
                          </v-list-item-title>
                          <v-list-item-subtitle>
                            {{ client.totalCA }}
                          </v-list-item-subtitle>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-card-text>
                </v-card>
              </v-card-text>
            </v-card>
          </v-col>
          <v-layout column class="col-sm-6 col-12 pt-0">
            <v-card>
              <v-card-title class="justify-center">
                Chiffre d'affaire HT
              </v-card-title>
              <v-card-subtitle class="text-center text-h5">
                62.235,08€
              </v-card-subtitle>
            </v-card>
            <v-spacer class="pa-3" />
            <v-card>
              <v-card-title class="justify-center">
                Commande moyenne HT
              </v-card-title>
              <v-card-subtitle class="text-center text-h5">
                2.005,08€
              </v-card-subtitle>
            </v-card>
          </v-layout>
          <v-col cols="12">
            <v-card>
              <v-card-title>
                <v-icon left>mdi-chart-areaspline</v-icon>
                Statistiques de ventes
              </v-card-title>
              <v-card-text>
                <v-row>
                  <v-col cols="6">
                    <v-img
                      src="/statistics-donut-chart.png"
                      contain
                      max-height="200px"
                    />
                  </v-col>
                  <v-col cols="1">
                    <v-divider vertical />
                  </v-col>
                  <v-col cols="5">
                    <v-img
                      src="/statistics-legend.png"
                      contain
                      max-height="200px"
                    />
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12" class="pb-0">
            <v-card>
              <v-card-title>
                <v-icon left>mdi-file-document-outline</v-icon>
                Factures
              </v-card-title>
              <v-card-text>
                <v-row>
                  <v-col cols="12" sm="6">
                    <v-card outlined>
                      <v-list-item two-line>
                        <v-list-item-content>
                          <v-list-item-subtitle
                            >Factures à recevoir</v-list-item-subtitle
                          >
                          <v-list-item-title class="text-h5 mb-1"
                            >25</v-list-item-title
                          >
                        </v-list-item-content>
                        <v-list-item-avatar
                          style="border-radius: 10px"
                          color="info"
                          size="60"
                        >
                          <v-icon
                            class="white--text"
                            size="45"
                            v-text="'mdi-file'"
                          ></v-icon>
                        </v-list-item-avatar>
                      </v-list-item>
                    </v-card>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-card outlined>
                      <v-list-item two-line>
                        <v-list-item-content>
                          <v-list-item-subtitle
                            >Factures en retard</v-list-item-subtitle
                          >
                          <v-list-item-title class="text-h5 mb-1"
                            >4</v-list-item-title
                          >
                        </v-list-item-content>
                        <v-list-item-avatar
                          style="border-radius: 10px"
                          color="warning"
                          size="60"
                        >
                          <v-icon
                            class="white--text"
                            size="45"
                            v-text="'mdi-clock'"
                          ></v-icon>
                        </v-list-item-avatar>
                      </v-list-item>
                    </v-card>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      lastOrders: [
        {
          client: 'Café des philosophes',
          priceTTC: '1100,67€',
          orderPicker: 'Michel',
          deliveryMan: null,
        },
        {
          client: 'Café des philosophes',
          priceTTC: '1100,67€',
          orderPicker: null,
          deliveryMan: null,
        },
        {
          client: 'Café des philosophes',
          priceTTC: '1100,67€',
          orderPicker: null,
          deliveryMan: 'Pascal',
        },
        {
          client: 'Café des philosophes',
          priceTTC: '1100,67€',
          orderPicker: null,
          deliveryMan: null,
        },
        {
          client: 'Café des philosophes',
          priceTTC: '1100,67€',
          orderPicker: null,
          deliveryMan: null,
        },
        {
          client: 'Café des philosophes',
          priceTTC: '1100,67€',
          orderPicker: null,
          deliveryMan: null,
        },
      ],
      topClients: [
        {
          name: 'Le Mélécasse',
          totalCA: '18.000€ HT',
        },
        {
          name: 'Le café des philosophes',
          totalCA: '14.000€ HT',
        },
        {
          name: 'Le café de la poste',
          totalCA: '10.000€ HT',
        },
      ],
    }
  },
}
</script>
