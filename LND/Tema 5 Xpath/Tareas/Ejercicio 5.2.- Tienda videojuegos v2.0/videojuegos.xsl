<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <head>
                <title>Inventario de Juegos</title>
                <style>
                    body { font-family: sans-serif; padding: 20px;}
                    table { border-collapse: collapse; width: 70%; }
                    th, td { border: 1px solid #444; padding: 10px; text-align: left; }
                    tr { background-color: #f2f2f2; }
                    .agotado {font-weight: bold; }
                    .usd {font-weight: bold; color: blue; }
                    .deluxe { font-style: italic; font-size: 0.85em; margin-left:
                    6px; }
                    .estrella { margin-left: 4px; }
                </style>
            </head>
            <body>
                <h2>Lista de Videojuegos</h2>
                <table>
                    <tr>
                        <th>Título</th>
                        <th>Consola</th>
                        <th>Precio</th>
                        <th>Género</th>
                    </tr>

                    <xsl:for-each select="tienda/videojuego">
                        <xsl:sort select="precio" data-type="number" order="descending" />
                        <tr>

                            <td>
                                <xsl:if test="titulo = 'Elden Ring'">
                                    <i>
                                        <xsl:value-of select="titulo" />
                                    </i>
                                </xsl:if>
                                <xsl:if test="titulo != 'Elden Ring'">
                                    <xsl:value-of select="titulo" />
                                </xsl:if>

                                <xsl:if test="@stock = 'no'">
                                    <span class="agotado"> — AGOTADO</span>
                                </xsl:if>
                            </td>

                            <td>
                                <xsl:if test="@consola = 'Switch'">
                                    <xsl:attribute name="style">background-color: #c0392b; color:
                                        #fff;</xsl:attribute>
                                </xsl:if>
                                <!-- Regla 5: PS5 → fondo azul -->
                                <xsl:if test="@consola = 'PS5'">
                                    <xsl:attribute name="style">background-color: #1a5276; color:
                                        #aad4f5;</xsl:attribute>
                                </xsl:if>
                                <xsl:value-of select="@consola" />
                            </td>

                            <td>
                                <xsl:if test="precio/@moneda = 'USD'">
                                    <span class="usd">
                                        <xsl:value-of select="precio" />
                                        <xsl:text> </xsl:text>
                                        <xsl:value-of select="precio/@moneda" />
                                    </span>
                                </xsl:if>
                                <xsl:if test="precio/@moneda != 'USD'">
                                    <xsl:value-of select="precio" />
                                    <xsl:text> </xsl:text>
                                    <xsl:value-of select="precio/@moneda" />
                                </xsl:if>

                                <xsl:if test="precio = 60">
                                    <span class="estrella">⭐</span>
                                </xsl:if>

                                <xsl:if test="precio &gt; 70">
                                    <span class="deluxe">- Edición Deluxe</span>
                                </xsl:if>
                            </td>
                            <td>
                                <xsl:value-of select="genero" />
                            </td>
                        </tr>
                    </xsl:for-each>

                </table>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>